dependencies:
    1) mysql
    2) python
    3) django
steps to compile:
    1) start mysql
    2) create schema called 'library_app_db',
    3) install python
    4) pip install django
    5) pip install django-extensions
    6) pip install django-tables2
    7) pip install django-staticfiles
steps to run:
    1) python manage.py makemigrations
    2) python manage.py migrate
    3) python manage.py runscript seed_db_from_csv --script-args <path/to/books.csv> books
    4) python manage.py runscript seed_db_from_csv --script-args <path/to/borrowers.csv> borrowers
    5) python manage.py runserver

# Django Library Management Application

A library management app written in Django for my database design class at UTD

## Getting Started


### Prerequisites

* mysql
* python3
* django
* django-extensions
* django-tables2
* django-staticfiles

```
pip install django
pip install django-extensions
pip install django-tables2
pip install django-staticfiles
```

## Deployment

```
1) python manage.py makemigrations
2) python manage.py migrate
3) python manage.py runscript seed_db_from_csv --script-args <path/to/books.csv> books
4) python manage.py runscript seed_db_from_csv --script-args <path/to/borrowers.csv> borrowers
5) python manage.py runserver
```

## Authors

* **Megan Yociss**