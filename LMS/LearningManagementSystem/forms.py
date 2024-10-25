# forms.py
from django import forms
from .models import Book, Members

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'status', 'cost', 'procurement_date']
        exclude = ['BookID'] 
        widgets = {
            'procurement_date': forms.DateInput(attrs={'type': 'date'}),
        }
class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['name', 'contact', 'address', 'aadhar', 'enroll_date', 'end_date', 'status', 'amount']
        widgets = {
            'enroll_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }