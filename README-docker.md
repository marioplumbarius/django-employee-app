# Django Employee APP
Employee Management application written in Pyhon (Django).

**Components:**
- admin panel to manage employees' data
- API to list, add and remove employees

***Note: to run the app using your local environment, head over [README.md](README.md)***

[![Build Status](https://travis-ci.org/marioluan/django-employee-app.svg?branch=master)](https://travis-ci.org/marioluan/django-employee-app)
[![codebeat badge](https://codebeat.co/badges/09d03419-d881-4ffb-a719-17566c9e9d1a)](https://codebeat.co/projects/github-com-marioluan-django-employee-app)
[![Coverage Status](https://coveralls.io/repos/github/marioluan/django-employee-app/badge.svg?branch=master)](https://coveralls.io/github/marioluan/django-employee-app?branch=master)
[![Dependency Status](https://gemnasium.com/badges/github.com/marioluan/django-employee-app.svg)](https://gemnasium.com/github.com/marioluan/django-employee-app)

---

**Pre-requisites:**
- docker (v1.13.0)
- docker-compose (v1.10.0-rc2)

## Run migrations
```bash
docker-compose run web python3 employeemanager/manage.py migrate
```

## Create superuser
```bash
docker-compose run web python3 employeemanager/manage.py createsuperuser
```

## Test
```bash
docker-compose run web coverage run --source='.' employeemanager/manage.py test staff.tests
```

## Code coverage report
```bash
docker-compose run web coverage html
# the report will be located at `htmlcov/index.html`
```

## Start app
```shell
docker-compose up
```

---

## API usage
To interact with the API, log in at [http://localhost:8000/staff/api-auth/](http://localhost:8000/staff/api-auth/) with the superuser created before. After log in, you might be redirected to an interactive interface.

## Admin
Head over [http://localhost:8000/staff/admin/](http://localhost:8000/staff/admin/) to access the admin.
