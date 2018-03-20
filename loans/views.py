from django.shortcuts import render
from django.template import RequestContext
from .forms import BorrowerForm, SearchForm
from .models import Borrower, Book_Loan, Fine
from .tables import LoanTable, FineTable
from collection.models import Book
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.db.models import IntegerField, Max, Sum
from django.shortcuts import redirect
from django.db.models.functions import Substr, Cast
from django_tables2 import RequestConfig
from django.db.models import Q
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    form = SearchForm()
    return render(request, 'loans/index.html', {'form': form})


def search(request):
    q = request.GET['text_to_search']
    loans = Book_Loan.objects.filter(Q(book_id=q) | Q(borrower_id=q) | Q(borrower__bname__icontains=q))
    table = LoanTable(loans)
    RequestConfig(request).configure(table)
    return render(request, 'loans/search_results.html', {'table': table})


def new(request):
    borrower = Borrower.objects.get(card_id=request.POST['card_id'])
    book = Book.objects.get(isbn=request.POST['book_id'])
    book_is_checked_out = Book_Loan.objects.filter(book_id=request.POST['book_id'], date_in=None).exists()
    response_data = []
    count = borrower.book_loan_set.filter(date_in=None).count()
    
    if count == 3:
        response_data.append({'level': 'danger', 'message': 'Member cannot check out more books!'})

    if book_is_checked_out:
        response_data.append({'level': 'danger', 'message': 'This book is checked out already!'})


    if not count > 3 and not book_is_checked_out:
        Book_Loan(book=book, borrower=borrower).save()
        response_data.append({'level': 'success', 'message': 'Book has been checked out.'})


    return JsonResponse({ 'messages': response_data })
 


@csrf_exempt
def check_in(request, loan_id):
    loan = Book_Loan.objects.get(loan_id=loan_id)
    loan.date_in = datetime.now()
    loan.save()
    return HttpResponse(status=200)



def new_member(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            
            max_card_num = Borrower.objects\
                            .annotate(id_as_int=Cast(Substr('card_id', 3), IntegerField()))\
                            .aggregate(Max('id_as_int'))\
                            .get('id_as_int__max')
                            
            member.card_id = 'ID' + format(max_card_num + 1, '06')
            member.save()
            messages.success(request, 'Added new member.')
        else:
            for error in form.errors:
                messages.error(request, error)

    else:
        form = BorrowerForm()

    return render(request, 'borrowers/new.html', {'form': form})


def fines(request):
    for loan in Book_Loan.objects.all():
        if not loan.date_in and loan.due_date < datetime.now().date():
            fine = Fine.objects.get(book_loan=loan)
            if not fine:
                fine = Fine(book_loan=loan)
            fine.amount = 0.25 * (datetime.today().date() - loan.due_date).days
            fine.save()
        elif loan.date_in and loan.date_in > loan.due_date:
            fine = Fine.objects.get(book_loan=loan)
            if not fine:
                fine = Fine(book_loan=loan)
            fine.amount = 0.25 * (loan.date_in - loan.due_date).days
            fine.save()

    fines = Fine.objects.filter(paid=False).values('book_loan__borrower').annotate(total_fines=Sum('amount'))
    table = FineTable(fines)
    return render(request, 'fines/fines.html', {'table': table})

@csrf_exempt
def pay(request, id):
    fine = Fine.objects.get(id=id)
    loan = Book_Loan.objects.get(fine=fine)
    response_data = []
    if loan.date_in:
        fine.paid = True
        fine.save()
        response_data.append({'level': 'success', 'message': 'Fine Paid'})
    else:
        response_data.append({'level': 'danger', 'message': 'Fine cannot be paid while book is checked out'})
    return JsonResponse({ 'messages': response_data })

