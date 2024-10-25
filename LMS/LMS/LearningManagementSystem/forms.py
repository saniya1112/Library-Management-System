# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'status', 'cost', 'procurement_date']
        exclude = ['BookID'] 
        widgets = {
            'procurement_date': forms.DateInput(attrs={'type': 'date'}),
        }
