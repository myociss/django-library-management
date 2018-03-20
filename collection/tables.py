import django_tables2 as tables
from .models import Book, Author

class BookTable(tables.Table):
    check_out = tables.TemplateColumn(template_name='books/checkout_button.html')

    class Meta:
        model = Book
        attrs = {'class': 'table'}
        fields = {'isbn', 'title', 'all_authors', 'check_out'}