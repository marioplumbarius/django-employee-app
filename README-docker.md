# Django Employee APP
Employee Management application written in Pyhon (Django).

**Components:**
- admin panel to manage employees' data
- API to list, add and remove employees

***Note: to run the app using your local environment, head over [README.md](README.md)***

---

**Pre-requisites:**
- docker (v1.12.6)
- docker-compose (v1.10)

## Run migrations
```shell
source .dockerenv
docker run \
    --rm \
    --name employeemanager_migrations \
    -v $HOST_DIR:/opt/app \
    $DOCKER_IMAGE \
    python3 employeemanager/manage.py migrate
```

## Create superuser with privileged access
```shell
source .dockerenv
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
source .dockerenv
docker run \
    --rm \
    --name employeemanager_test \
    -v $HOST_DIR:/opt/app \
    $DOCKER_IMAGE \
    python3 employeemanager/manage.py test
```

## Start app
```shell
docker-compose up
```

---

## API usage
To interact with the API, log in at http://localhost:8000/staff/api-auth/  
with the superuser created before. After log in, you might be redirected   
to an interactive interface.

## Admin
Head over http://localhost:8000/staff/admin/ to access the admin.
