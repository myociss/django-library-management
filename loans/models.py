from django.db import models
from datetime import datetime, timedelta
from collection.models import Book

# Create your models here.
class Borrower(models.Model):
    card_id = models.CharField(primary_key=True, max_length=8, null=False)
    ssn = models.CharField(max_length=9, unique=True, null=False)
    bname = models.CharField(max_length=40, null=False)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=40, null=False)
    state = models.CharField(max_length=2, null=False)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=40)    
    books = models.ManyToManyField(Book, through='Book_Loan')


class Book_Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    book = models.ForeignKey('collection.Book', on_delete=models.PROTECT)
    borrower = models.ForeignKey('Borrower', on_delete=models.PROTECT)
    #fine = models.ForeignKey('Fine', on_delete=models.PROTECT)
    date_out = models.DateField(auto_now=True)
    due_date = models.DateField(default=datetime.now()+timedelta(days=14))
    date_in = models.DateField(null=True)

class Fine(models.Model):
    book_loan = models.OneToOneField(Book_Loan, on_delete=models.PROTECT)
    amount = models.FloatField(default=0.0)
    paid = models.BooleanField(default=False)
