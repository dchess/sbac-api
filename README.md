# SBAC API Server

## Purpose:

This app is designed to serve up SBAC (Smarter Balanced Assessment) data for California in an easy to query format for simple consumption by education developers as well as a reporting front end with easy to interpret results for general audiences.

**Data Source**: [CAASPP SBAC Results](https://caaspp.cde.ca.gov/sb2017/default)

## Dependencies:

- Django 2.0
- Django Rest Framework
- Python 3.5
- Pipenv
- PostgreSQL 10

## Getting Started

### Install Dependencies

```
$ pip install pipenv
$ pipenv install
```

### Setup Database

Run the automated PostgreSQL setup script. You will need to supply a database name, user, and password at runtime.

```
$ ./psql.sh
```

### Migrate Database

```
$ pipenv run python manage.py migrate
```

### Run the Test Suite

```
$ pipenv run python manage.py test
```

### Run the Local Server

```
$ pipenv run python manage.py runserver
```
