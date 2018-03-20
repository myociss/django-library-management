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
* Create schema called library_app_db using mysql command line
* Edit settings.py to add mysql user and password information.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runscript seed_db_from_csv --script-args <path/to/books.csv> books
python manage.py runscript seed_db_from_csv --script-args <path/to/borrowers.csv> borrowers
python manage.py runserver
```

## Screenshots
* collection index
![collection index](/screenshots/collection_index.PNG?raw=true "collection index")

* search results styled with tables2
![collection table](/screenshots/search_collection.PNG?raw=true "search results styled with tables2")

* form to add a new library member
![member form](/screenshots/new_member.PNG?raw=true "form to add a new library member")

* loan table display
![loan table](/screenshots/loans_search.PNG?raw=true "loan table display")

## Authors

* **Megan Yociss**