import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from databot import DataBot
from welcome import WelcomeMessage
from pathlib import Path
from dotenv import load_dotenv
import boto3
__TableName__ = "billgist-slack-bot"
Primary_Coloumn_Name = "user_id"
Sort_Key = "channel_id"
client = boto3.resource('dynamodb', region_name='us-west-2')
table = client.Table(__TableName__)




env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injestion.
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACKBOT_TOKEN"))
BOT_ID = slack_web_client.api_call("auth.test")['user_id']
welcome_messages = {}


def fetch_data_action(channel, action=None, **kwargs):
    """Determine which action to perform based on parameter. For roll die if
    a kwarg of sides is passed in and it's a valid integer roll a dSIDES die
    """
    # Create a new CoinBot
    if 'integration_id' not in welcome_messages[channel]:
        return
    integration_id = welcome_messages[channel]['integration_id']
    random_bot = DataBot(channel, integration_id)
    if action == "daily":
        message = random_bot.get_daily_data()
    elif action == "monthly":
        message = random_bot.get_monthly_data()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)

def send_welcome_message(channel, user):
    if channel not in welcome_messages:
        welcome_messages[channel] = {}
    if user in welcome_messages[channel]:
        return
    welcome = WelcomeMessage(channel, user)
    message = welcome.get_message()
    response = slack_web_client.chat_postMessage(**message)
    welcome.timestamp = response['ts']
    welcome_messages[channel][user] = welcome

def add_integration(channel, user, text):
    if user not in welcome_messages[channel] and user != BOT_ID:
        return
    data = DataBot(channel, text)
    message = data.set_integration(text)
    result = message['result']
    if result:
        welcome_messages[channel]['integration_id'] = text
    message = message['message']
    response = slack_web_client.chat_postMessage(**message)
    data.timestamp = response['ts']
    welcome_messages[channel][user] = data


# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text,
    simulate a coin flip and send the result.
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")
    # Get the channel ID from the event that came through
    channel_id = event.get("channel")
    # Get the user ID from the event that came through
    user_id = event.get('user')

    if user_id != None and BOT_ID != user_id:
        table.put_item(
            Item={
                Primary_Coloumn_Name: user_id,
                Sort_Key: channel_id
            }
        )
        if "daily data" in text.lower():
            # Fetch daily data
            return fetch_data_action(channel_id, action="daily")
        elif "monthly data" in text.lower():
            # Fetch monthly data
            return fetch_data_action(channel_id, action="monthly")
        elif text.lower() == 'start':
            send_welcome_message(channel_id, user_id)
        else:
            add_integration(channel_id, user_id, text)

@slack_events_adapter.on("reaction_added")
def reaction_added(payload):
    # Get the event data from the payload
    event = payload.get("event", {})
    # Get the channel ID from the event that came through
    channel_id = event.get('item', {}).get("channel")
    # Get the user ID from the event that came through
    user_id = event.get('user')
    if f'{channel_id}' not in welcome_messages:
        return
    welcome = welcome_messages[f'{channel_id}'][user_id]
    welcome.completed = True
    welcome.channel = channel_id
    message = welcome.get_message()
    updated_message = slack_web_client.chat_update(**message)
    welcome.timestamp = updated_message['ts']

def fetch_data():
    response = table.scan()
    print(response)


if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())
    fetch_data()

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=8080)