# Django Employee APP
Employee Management application written in Pyhon (Django).

**Components:**
- admin panel to manage employees' data
- API to list, add and remove employees

***Note: to run the app using Docker, head over README-docker.md***

---

**Components:**
- admin panel to manage employees' data
- API to list, add and remove employees

**Pre-requisites:**
- python3 (v3.5)
- python-pip3 (v9.0.1)

## Install dependencies
```shell
pip3 install -r requirements.txt
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
python manage.py test staff
```

## Start app (development mode)
```shell
python3 manage.py runserver localhost:8000
```
---

## API usage
To interact with the API, log in at http://localhost:8000/staff/api-auth/  
with the superuser created before. After log in, you might be redirected   
to an interactive interface.

## Admin
Head over http://localhost:8000/staff/admin/ to access the admin.
