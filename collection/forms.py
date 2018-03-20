from django import forms

class BookForm(forms.Form):
    text_to_search = forms.CharField(label='Search', max_length=100)
    
class BookLoanForm(forms.Form):
    card_id = forms.CharField(label='Card ID', max_length=100)