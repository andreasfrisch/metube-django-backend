All: start

build:
	docker build -t metube backend/

test:
	cd backend/metube && python manage.py test --settings=metube.settings.test

start: build
	docker-compose up -d
	docker-compose exec api python manage.py migrate

stop:
	docker-compose down

development:
	cd backend/metube && python manage.py makemigrations --settings=metube.settings.test
	cd backend/metube && python manage.py migrate --settings=metube.settings.test
	cd backend/metube && python manage.py runserver --settings=metube.settings.test