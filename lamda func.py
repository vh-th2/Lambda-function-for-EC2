import json
import boto3


ec2 = boto3.client('ec2')

def lambda_handler(event, context):
   print(event)
   
   user = event['userIdentity']['userName']
   eventID = event['eventID']  
  
   response = ec.create_tags(
    DryRun=True|False,
    Resources=[
        eventID
    ],
    Tags=[
        {
            'Key': 'User',
            'Value': user
        },
    ]
)
   return 
   
   
  