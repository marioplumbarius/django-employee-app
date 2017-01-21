# Django Employee APP
Employee Management application written in Pyhon (Django).

**Components:**
- admin panel to manage employees' data
- API to list, add and remove employees

***Note: to run the app using Docker, head over [README-docker.md](README-docker.md)***

[![Build Status](https://travis-ci.org/marioluan/django-employee-app.svg?branch=master)](https://travis-ci.org/marioluan/django-employee-app)
[![codebeat badge](https://codebeat.co/badges/09d03419-d881-4ffb-a719-17566c9e9d1a)](https://codebeat.co/projects/github-com-marioluan-django-employee-app)
[![Coverage Status](https://coveralls.io/repos/github/marioluan/django-employee-app/badge.svg?branch=master)](https://coveralls.io/github/marioluan/django-employee-app?branch=master)
[![Dependency Status](https://gemnasium.com/badges/github.com/marioluan/django-employee-app.svg)](https://gemnasium.com/github.com/marioluan/django-employee-app)

---

**Pre-requisites:**
- python3 (v3.5)
- python-pip3 (v9.0.1)

## Install dependencies
```shell
pip3 install -r requirements.txt
pip3 install -r requirements-test.txt
```

## Go to employeemanager directory
Before running any of the following commands, you should
cd into employeemanager directory:
```shell
cd employeemanager
```

## Run migrations
```shell
python3 manage.py migrate
```

## Create superuser with privileged access
```shell
python3 manage.py createsuperuser
```

## Test
```shell
coverage run --source='.' employeemanager/manage.py test staff.tests
```

## Code coverage report
*Note: Run this command only after running the test suite with the command above.*
```shell
coverage html
# the report will be located at `htmlcov/index.html`
```

## Start app
```shell
python3 manage.py runserver localhost:8000
```

---

## API usage
To interact with the API, log in at [http://localhost:8000/staff/api-auth/](http://localhost:8000/staff/api-auth/) with the superuser created before. After log in, you might be redirected to an interactive interface.

## Admin
Head over [http://localhost:8000/staff/admin/](http://localhost:8000/staff/admin/) to access the admin.
