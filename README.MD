# Boilerplate Project

## Project Overview

![python](https://img.shields.io/badge/-python-grey?style=for-the-badge&logo=python&logoColor=white&labelColor=306998)
![django](https://img.shields.io/badge/-django-grey?style=for-the-badge&logo=django&logoColor=white&labelColor=092e20)
![postgresql](https://img.shields.io/badge/postgre-SQL-%23000.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![linux](https://img.shields.io/badge/linux-grey?style=for-the-badge&logo=linux&logoColor=white&labelColor=072c61)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

### Language: python 3.10 +

### Frameworks : Django 4+, DjangoRestFramework 3.12 +

### Database : postgresql 12+

### Project Setup

#### Create Database

```bash
>>> create role project_user with login password 'password';
>>> create database project_db with owner project_user;
```

#### Django install

```bash
>>> git clone https://github.com/mark-akbarov/test-todo-app/
>>> python -m venv .venv
>>> source .venv/bin/activate
>>> pip install -r requirements/local.txt
>>> cd src
>>> python manage.py migrate
>>> python3 manage.py runserver
```

#### Project endpoints

Auth:
    signup - api/v1/signup/
    login  - api/v1/login/

Todo:
    create - api/v1/tasks/
    read   - api/v1/tasks/1/
    update - api/v1/tasks/1/
    delete - api/v1/tasks/1/
    current - api/v1/tasks/
    completed - api/v1/tasks/completed/
