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
![alt text](screenshots/collection_index.png "collection index")
![alt text](screenshots/search_collection.png "search results styled with tables2")
![alt text](screenshots/new_member.png "form to add a new library member")
![alt text](screenshots/loans_search.png "loan table display")

## Authors

* **Megan Yociss**