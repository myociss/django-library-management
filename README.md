# Django Library Management Application

A library management app written in Django for my database design class at UTD

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
python manage.py makemigrations
python manage.py migrate
python manage.py runscript seed_db_from_csv --script-args <path/to/books.csv> books
python manage.py runscript seed_db_from_csv --script-args <path/to/borrowers.csv> borrowers
python manage.py runserver
```

## Authors

* **Megan Yociss**