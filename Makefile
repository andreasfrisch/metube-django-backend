All: start-local

build:
	docker build -t metube-api metube/
	docker build -t metube-nginx nginx/

start-local: apidocs test
	docker-compose up -d nginx

apidocs:
	docker run --rm -v $(CURDIR)/metube/src:/raml mattjtodd/raml2html -i raml/metube/authentication/auth_api.raml -o raml/docs/auth_api.html

stop:
	docker-compose down

test: build
	docker-compose run test

dev: start-local
	docker-compose exec api python manage.py loaddata fixture.json


# Following is AWS operations

create-cluster:
	aws --profile awscli --region eu-central-1 ecs create-cluster --cluster-name metube-cluster

register-task:
	aws --profile awscli --region eu-central-1  ecs register-task-definition --cli-input-json file://./metube-backend-task.json
# de-register
# aws --profile awscli --region eu-central-1 ecs deregister-task-definition --task-definition <taskName:revision>

list-tasks:
	aws --profile awscli --region eu-central-1 ecs list-task-definitions

register-service:
	aws --profile awscli --region eu-central-1 ecs create-service --cluster metube-cluster --service-name metube-service \
	--task-definition metube-api-task:3 --desired-count 1 --launch-type "FARGATE" \
	--load-balancers targetGroupArn=arn:aws:elasticloadbalancing:eu-central-1:624540041426:targetgroup/metube-target-group/91303693a3c494c4,containerName=metube-nginx,containerPort=443 \
	--network-configuration "awsvpcConfiguration={subnets=[subnet-61938608,subnet-edf2c4a7,subnet-9b3a16e0],securityGroups=[sg-1f438977],assignPublicIp='ENABLED'}"

list-services:
	aws --profile awscli --region eu-central-1 ecs list-services --cluster metube-cluster

describe-service:
	aws --profile awscli --region eu-central-1 ecs describe-services --cluster metube-cluster --services metube-service
