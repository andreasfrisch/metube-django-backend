All: start

build:
	docker build -t metube-api metube/
	docker build -t metube-nginx nginx/

start: build
	docker-compose up -d nginx
	docker-compose exec api python manage.py makemigrations
	docker-compose exec api python manage.py migrate

stop:
	docker-compose down

test: build
	docker-compose run test

dev: start
	docker-compose exec api python manage.py loaddata fixture.json
