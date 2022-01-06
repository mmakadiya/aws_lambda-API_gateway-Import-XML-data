import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print("V.1")
    print("========================")
    print(event)
    print("========================")
    
    s3 = boto3.resource("s3")
    s3.Bucket("my-files-maulik").put_object(Key = "MyFirstFile.xml", Body = event['body'])
    
    print("**********body = " + event['body'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
