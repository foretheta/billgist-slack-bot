import boto3
__TableName__ = "billgist-slack-bot"
Primary_Coloumn_Name = "user_id"
Sort_Key = "channel_id"
client = boto3.resource('dynamodb', region_name='us-west-2')
table = client.Table(__TableName__)
class DataBot:

    # Create a constant that contains the default text for the message
    MESSAGE_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ""
        },
    }
    MONTHLY_DATA = {
        "dbfb3f08-a6c3-4c76-a104-40f7a9d243d6": {
            "data": {
                "2021-12-09": {
                    "AWS Amplify": 0.49,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.98,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.1,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 8.63,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.01,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.57,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 17.89
                },
                "2021-12-08": {
                    "AWS Amplify": 0.37,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.81,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.08,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 8.62,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.57,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 17.56
                },
                "2021-12-05": {
                    "AWS Amplify": 0.02,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.39,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.07,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 6.94,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.57,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 15.1
                },
                "2021-12-04": {
                    "AWS Amplify": 0.02,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.39,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.07,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 6.95,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.57,
                    "Tax": 0.07,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 15.18
                },
                "2021-12-07": {
                    "AWS Amplify": 0.51,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.52,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.07,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 7.08,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.54,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 15.84
                },
                "2021-12-06": {
                    "AWS Amplify": 1.39,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.41,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.07,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 6.93,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.57,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 16.48
                },
                "2021-12-01": {
                    "AWS Amplify": 0.45,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.36,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "AWS Support (Business)": 100.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.01,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.17,
                    "Amazon Elastic Compute Cloud - Compute": 10.07,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Registrar": 19.0,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 12.9,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.5,
                    "Tax": 16.75,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 167.26
                },
                "2021-12-12": {
                    "AWS Amplify": 0.03,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.54,
                    "AWS Data Pipeline": 0.37,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.12,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon DynamoDB": 0.08,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 1.94,
                    "Amazon Elastic Compute Cloud - Compute": 8.22,
                    "Amazon Elastic Load Balancing": 0.52,
                    "Amazon Monitron": 0.25,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.0,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 0.03,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.55,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 12.68
                },
                "2021-12-11": {
                    "AWS Amplify": 0.02,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.54,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon DynamoDB": 0.08,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 8.59,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.57,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 16.91
                },
                "2021-12-03": {
                    "AWS Amplify": 0.65,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.24,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.01,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 6.94,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.55,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 15.51
                },
                "2021-12-02": {
                    "AWS Amplify": 0.11,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.52,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon Cognito": 0.0,
                    "Amazon DynamoDB": 0.01,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 7.64,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.5,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 15.89
                },
                "2021-12-13": {
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 0.0
                },
                "2021-12-10": {
                    "AWS Amplify": 0.02,
                    "AWS CloudTrail": 0.0,
                    "AWS Cost Explorer": 0.54,
                    "AWS Data Pipeline": 0.39,
                    "AWS Glue": 0.0,
                    "AWS Key Management Service": 0.13,
                    "AWS Lambda": 0.0,
                    "AWS Secrets Manager": 0.0,
                    "Amazon API Gateway": 0.0,
                    "Amazon CloudFront": 0.0,
                    "Amazon DynamoDB": 0.08,
                    "Amazon EC2 Container Registry (ECR)": 0.0,
                    "Amazon ElastiCache": 0.01,
                    "EC2 - Other": 4.08,
                    "Amazon Elastic Compute Cloud - Compute": 8.6,
                    "Amazon Elastic Load Balancing": 0.54,
                    "Amazon Monitron": 0.27,
                    "Amazon Pinpoint": 0.03,
                    "Amazon Relational Database Service": 0.01,
                    "Amazon Route 53": 0.0,
                    "Amazon Simple Email Service": 0.0,
                    "Amazon Simple Notification Service": 0.0,
                    "Amazon Simple Queue Service": 0.0,
                    "Amazon Simple Storage Service": 1.66,
                    "Amazon SimpleDB": 0.0,
                    "AmazonCloudWatch": 0.5,
                    "Tax": 0.0,
                    "credits": {
                        "total": -0.0
                    },
                    "Total_Credits": 0.0,
                    "sum": 16.85
                }
            },
            "services": [
                "AWS Amplify",
                "AWS CloudTrail",
                "AWS Cost Explorer",
                "AWS Data Pipeline",
                "AWS Glue",
                "AWS Key Management Service",
                "AWS Lambda",
                "AWS Secrets Manager",
                "Amazon API Gateway",
                "Amazon CloudFront",
                "Amazon Cognito",
                "Amazon DynamoDB",
                "Amazon EC2 Container Registry (ECR)",
                "Amazon ElastiCache",
                "EC2 - Other",
                "Amazon Elastic Compute Cloud - Compute",
                "Amazon Elastic Load Balancing",
                "Amazon Monitron",
                "Amazon Pinpoint",
                "Amazon Relational Database Service",
                "Amazon Route 53",
                "Amazon Simple Email Service",
                "Amazon Simple Notification Service",
                "Amazon Simple Queue Service",
                "Amazon Simple Storage Service",
                "Amazon SimpleDB",
                "AmazonCloudWatch",
                "Tax",
                "AWS Support (Business)",
                "Amazon Registrar"
            ],
            "total": 343.16,
            "credits_total": -0.0,
            "name": "Test Integration"
        }
    }

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, user, channel):
        self.user = user
        self.channel = channel
        self.timestamp = ''
        self.integration_id = ''

    # Fetch daily data for the user
    def get_daily_data(self):
        message = "This is daily data"

        self.MESSAGE_BLOCK["text"]["text"] = message
        return {
            "channel": self.channel,
            "blocks": [
                self.MESSAGE_BLOCK
            ],
        }

    # Fetch daily data for the user
    def get_monthly_data(self):
        if(self.integration_id == ''):
            monthly_text = "Integration Id not found"
        else:
            monthly_total = self.MONTHLY_DATA[self.integration_id]["total"]
            integration_name = self.MONTHLY_DATA[self.integration_id]["name"]
            credits = self.MONTHLY_DATA[self.integration_id]["credits_total"]

            monthly_text = {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': (
                        "*Here is your monthly data! *  \n\n"
                        f"Integration *{integration_name}* has the monthly total of ${monthly_total} \n\n"
                        f"your total credits are: ${credits}"
                        )
                }
            }

        return {
            "channel": self.channel,
            "blocks": [
                monthly_text
            ],
        }

    def set_integration(self, integration_id):
        data = table.get_item(
            Key={
                Primary_Coloumn_Name: self.user,
                Sort_Key: self.channel
            }
        )["Item"]
        new_integration_id = data["integration_id"]
        if integration_id == new_integration_id:
            self.integration_id = new_integration_id
            message = "*Integration ID has been set!*"
            result = True
        else:
            message = "*Invalid integration ID, please send again!*"
            result = False
        return {
            'result': result,
            'message': {
            'ts': self.timestamp,
            'channel': self.channel,
            'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': message
                }
            }
            ]}
        }
