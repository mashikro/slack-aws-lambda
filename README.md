# <h1>slack-aws-lambda</h1>
<h2>Send a slack message on a fixed schedule using AWS Lambda, CloudWatch Events and Incoming Webhooks.</h2>


- Step 1: Create a lambda function here: https://console.aws.amazon.com/lambda/ <br>
- Step 2: Copy and paste code from main.py into your lambda function code editor. Feel free to edit the type of message.<br>
- Step 2.1: Note I am using AWS environment variable to store my webhook. If you scroll past the code editor you should see it.<br>
- Step 3: Set up a schedule using Cloudwatch Events. Follow this tutorial: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html<br>
