# Contributing

Follow [github flow](https://guides.github.com/introduction/flow/) to contribute.

In summary:

## 1. clone the repository
```shell
git clone https://github.com/marioluan/django-employee-app.git
```

## 2. create a feature branch
```shell
git checkout -b <descriptive_branch_name>
```

## 3. add commits
**Before commiting new changes:**

### 3.1. run the static code analyzer
```shell
flake8
```
**Note: Fix reported errors.**

### 3.2. run unit tests
```shell
coverage run --source='.' employeemanager/manage.py test staff
```
**Note: Write unit tests for new code and modify existing ones, where necessary.**

### 3.4. generate and check code coverage report
Code coverage report will be automatically generated to `htmlcov/index.html`.
```shell
coverage html
```

**Note: New code cannot decrease the code coverage percentage.**

### 3.5. commit new changes
```shell
$ git commit -m <short_and_descriptive_message>
```
**Note: No commits can break the branch.**

## 4. open a pull request
## 5. discuss and review your code
## 6. deploy your changes
