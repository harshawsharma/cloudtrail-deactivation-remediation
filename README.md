# cloudtrail-deactivation-remediation

This Lambda code and SAM template together ensure that CloudTrail Logging is not disabled by accident.

##Pre-requisites
- Cloudtrail should be already configured with logging turned ON.

## The SAM template creates the following resources:
- 1 Lambda Function 
- 1 IAM Role with 1 Managed Policy and 1 Custom Policy
- 1 CloudWatch Event that triggers the Lambda function when it sees the StopLogging event from CloudTrail


