import sys
import csv
from pathlib import Path
from collection.models import Book, Author
from loans.models import Borrower


def run(csv_file, model_name):

    if not csv_file:
        print('usage: python manage.py runscript seed_db_from_csv.py --script-args <yourfile.csv> <data_type>')
    elif not Path(csv_file).is_file():
        print(csv_file + ' not found')
    elif not csv_file.split('.')[-1] == 'csv':
        print('file must be in csv format')
    else:
        if model_name == 'books':
            load_books(csv_file)
        elif model_name == 'borrowers':
            load_borrowers(csv_file)
        else:
            print('data type should be either books or borrowers')
        

def load_books(books_file):

    with open(books_file, encoding="latin1") as books:
        rows = csv.DictReader(books, delimiter='\t')
        for row in rows:
            book = Book(isbn=row['ISBN10'], title=row['Title'])
            book.save()
            author_names = row['Author'].split(',') #Author(name=row['Author'])
            for author_name in author_names:
                author = Author.objects.all().filter(name=author_name).first()
                if not author:
                    author = Author(name=author_name)
                    author.save()
                author.books.add(book)
            #author.save()
            #author.books.add(book)

def load_borrowers(borrowers_file):
    
    with open(borrowers_file, encoding='latin1') as borrowers:
        rows = csv.DictReader(borrowers)
        for row in rows:
            borrower = Borrower(card_id=row['ID0000id'], ssn=row['ssn'].replace('-', ''), 
            bname = row['first_name'] + ' ' row['last_name'],
            address=row['address'], city=row['city'], state=row['state'], 
            # not clean
            phone=row['phone'].replace('-', '').replace('(', '').replace(')', '').replace(' ', ''),
            email=row['email'])
            borrower.save()
