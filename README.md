## cloudtrail-deactivation-remediation

This Lambda code and SAM template together ensure that CloudTrail Logging is not disabled by accident.

### Pre-requisites
- Cloudtrail should be already configured with logging turned ON.


### The SAM template creates the following resources:
- 1 Lambda Function 
- 1 IAM Role with 1 Managed Policy and 1 Custom Policy
- 1 CloudWatch Event that triggers the Lambda function when it sees the StopLogging event from CloudTrail


### High level flow
Once set up, this setup would work as follows:

- Customer accidentaly turns OFF logging 
- Cloudwatch event catches this and immediately triggers the Lambda function 
- Lambda calls the StartLogging API to turn logging back ON


### Additional Considerations

- Email triggers can be setup at the Cloudwatch event side to notify of this activity.
- The code can be expanded to provide SNS notification