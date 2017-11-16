import boto3

def lambda_handler(event, context):
    #additional check to ensure only StopLogging Events are processed
    if event['detail']['eventName'] == 'StopLogging':
        #get the trail arn from the incoming json payload in the event field
        trail_arn = event['detail']['requestParameters']['name']
        
        #create low level client for cloudtrail
        cloudtrail_client = boto3.client('cloudtrail')
        
        #use the cloudtrail client and trail arn to start logging
        response = cloudtrail_client.start_logging(
        Name=trail_arn
        )
        
    else:
        response = "This is an invalid function invocation"
    
    return response