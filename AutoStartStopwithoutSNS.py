import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    tag_key = 'AutoStartStop'
    tag_value = 'True'

    # Retrieve all EC2 instances with the specified tag
    instances = ec2.describe_instances(
        Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}]
    )
    
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_ids.append(instance_id)  # Fixed variable name
            
    if not instance_ids:
        print("No instances found with the specified tag AutoStartStop=True.")
        return {
            'statusCode': 200,
            'body': 'No instances found with the specified tag.'
        }
    
    # Get action from event, default to 'stop'
    action = event.get('action', 'stop').lower()
    
    if action == 'start':
        response = ec2.start_instances(InstanceIds=instance_ids)
        print(f'Started instances: {instance_ids}')
        return {
            'statusCode': 200,
            'body': f'Successfully started instances: {instance_ids}'
        }
        
    elif action == 'stop':
        response = ec2.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped instances: {instance_ids}')
        return {
            'statusCode': 200,
            'body': f'Successfully stopped instances: {instance_ids}'
        }
        
    else:
        print("Invalid action specified. Use 'start' or 'stop'.")
        return {
            'statusCode': 400,
            'body': "Invalid action specified. Use 'start' or 'stop'."
        }