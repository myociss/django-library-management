from django import forms
from .models import Borrower

class SearchForm(forms.Form):
    text_to_search = forms.CharField(label='Search', max_length=100)

# Create the form class.
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['ssn', 'bname', 'address', 'city', 'state', 'phone', 'email']
