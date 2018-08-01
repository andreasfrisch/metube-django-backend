import boto3
import time

client = boto3.client('ecs')

response = client.update_service(
    cluster='metube',
    service='metube',
    desiredCount=0,
    taskDefinition='metube'
)

tasks = client.list_tasks(
    cluster='metube',
    desiredStatus='RUNNING',
)['taskArns']

for t in tasks:
    client.stop_task(
        cluster='metube',
        task=t,
        reason='redeploy'
    )

# Waiting for service to end in stable state
time.sleep(60)

response = client.update_service(
    cluster='metube',
    service='metube',
    desiredCount=1,
    taskDefinition='metube',
    deploymentConfiguration={
        'maximumPercent': 200,
        'minimumHealthyPercent': 0
    },
    forceNewDeployment=True
)