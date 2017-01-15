# Django Employee APP
Employee Management application written in Pyhon (Django).

**Components:**
- admin panel to manage employees' data
- API to list, add and remove employees

***Note: to run the app using your local environment, head over [README.md](README.md)***

[![Build Status](https://travis-ci.org/marioluan/django-employee-app.svg?branch=master)](https://travis-ci.org/marioluan/django-employee-app)
[![Code Climate](https://codeclimate.com/github/marioluan/django-employee-app/badges/gpa.svg)](https://codeclimate.com/github/marioluan/django-employee-app)
[![Test Coverage](https://codeclimate.com/github/marioluan/django-employee-app/badges/coverage.svg)](https://codeclimate.com/github/marioluan/django-employee-app/coverage)
[![Issue Count](https://codeclimate.com/github/marioluan/django-employee-app/badges/issue_count.svg)](https://codeclimate.com/github/marioluan/django-employee-app)
[![Dependency Status](https://gemnasium.com/badges/github.com/marioluan/django-employee-app.svg)](https://gemnasium.com/github.com/marioluan/django-employee-app)


---

**Pre-requisites:**
- docker (v1.12.6)
- docker-compose (v1.10)

## Load environment variables
**IMPORTANT:** this must be done before any subsequent step.
```shell
source .dockerenv
```

## Build the Docker image
```shell
docker build -t $DOCKER_IMAGE .
```

## Run migrations
```shell
touch employeemanager/db.sqlite3
docker run \
    --rm \
    --name employeemanager_migrations \
    -v $HOST_DIR:/opt/app \
    $DOCKER_IMAGE \
    python3 employeemanager/manage.py migrate
```

## Create superuser with privileged access
```shell
docker run \
    --rm \
    -ti \
    --name employeemanager_createsuperuser \
    -v $HOST_DIR:/opt/app \
    $DOCKER_IMAGE \
    python3 employeemanager/manage.py createsuperuser
```

## Test
```shell
docker run \
    --rm \
    --name employeemanager_test \
    -v $HOST_DIR:/opt/app \
    $DOCKER_IMAGE \
    python3 employeemanager/manage.py test staff
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
