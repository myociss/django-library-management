import django_tables2 as tables
from .models import Book_Loan, Fine

class LoanTable(tables.Table):
    check_in = tables.TemplateColumn(template_name='loans/check_in_button.html')
    pay_fine = tables.TemplateColumn(template_name='loans/pay_fine_button.html')

    class Meta:
        model = Book_Loan
        attrs = {'class': 'table'}
        fields = {'book_id', 'borrower_id', 'date_out', 'due_date', 'date_in', 'check_in'}

class FineTable(tables.Table):

    class Meta:
        model = Fine
        attrs = {'class': 'table'}
        fields = {'book_loan__borrower', 'total_fines'}
