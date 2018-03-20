from django.db import models
# from loans.models import Book_Loan

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    #loans = models.ManyToOneRel(Book_Loans)
    
    def __str__(self):
        return '%s, %s, (%s)' % (
            self.isbn,
            self.title, 
            ', '.join(author.name for author in self.author_set.all())
            )

    @property
    def all_authors(self):
        return ', '.join([x.name for x in self.author_set.all()])

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
