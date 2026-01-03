# Automated AWS EC2 Cost Optimization Framework with EventBridge Scheduler, Lambda, SNS, and IAM



## For more projects, check out  
[https://harishnshetty.github.io/projects.html](https://harishnshetty.github.io/projects.html)

[![Video Tutorial](https://github.com/harishnshetty/image-data-project/blob/ccd5b46f956ad4cea6b16d3e03c9b2a236ecb107/stale-ec2.jpg)](https://youtu.be/BgyYqUXuHuk?si=Gi6vkxhnVJQBILkG)


## Production-Grade EC2 Auto Start–Stop System for Cost Optimization Using AWS Serverless Services

### Tags
`Autostartstop = True`

### lambda time out
5 min  
Runtime python3.14

### IAM ROLE inline policy

- `ec2:DescribeInstances`
- `ec2:StartInstances`
- `ec2:StopInstances`
- `sns:Publish`


### test case
- `test->action=stop`
- `test->action=start`

### event bridge scheduler
start at 8 am  
stop at 6 pm

### start scheduler
`00 8 ? JAN-DEC MON-FRI *`

### stop scheduler
`00 18 ? JAN-DEC MON-FRI *`

### payload
```json
{
    "action": "stop"
}
```

### payload
```json
{
    "action": "start"
}
```


### Delete the resources

1. delete the lambda function
2. delete the iam role
3. delete the event bridge scheduler
4. delete the sns topic
5. delete the ec2 instances