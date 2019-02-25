All: start

build:
	docker build -t metube-api metube/
	docker build -t metube-nginx nginx/

start: apidocs build
	docker-compose up -d nginx
	docker-compose exec api python manage.py makemigrations
	docker-compose exec api python manage.py migrate

apidocs:
	docker run --rm -v $(CURDIR)/metube/src:/raml mattjtodd/raml2html -i raml/metube/authentication/auth_api.raml -o raml/docs/auth_api.html

stop:
	docker-compose down

test: build
	docker-compose run test

dev: start
	docker-compose exec api python manage.py loaddata fixture.json
