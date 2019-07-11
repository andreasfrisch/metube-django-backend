[![CircleCI](https://circleci.com/gh/andreasfrisch/metube-django-backend.svg?style=svg)](https://circleci.com/gh/andreasfrisch/metube-django-backend)

# Metube Django Backend
This is a Django powered monolithic backend for the metube project.
This acts solely as an API and most frontend work is handled elsewhere.

## Getting Started

### Software requirements
* docker
* docker-compose
* make (optional)

### Development
Simply run

	make dev

from the root of the project.

This will spin up all required containers, run migrations, and apply a fixture adding a superuser.
The credentials for the superuser is

	username: test-admin
	password: test1234

### Tests
Simply run

	make test

from the root of the project.

This will build the containers and run all tests.

### Updating containers
This solution is intended to be completely isolated through dockerization.
Updating code can be achieved using docker volumes, but I prefer simply re-running

	make dev

or

	make test

in order to rebuild and relaunch updated containers.

This is fast enough for regular changes during development while not breaking encapsulation.
