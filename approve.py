import boto3
from botocore.exceptions import ClientError
from sys import argv
import requests



RECIPIENT = "sachin.saini@cloverbaytechnologies.com"
SENDER = "yogesh.p@cloverbaytechnologies.com"
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"


# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("\r\n"
            )
# The HTML body of the email.
<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
              <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>
