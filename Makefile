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
