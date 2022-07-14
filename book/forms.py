from django import forms 
from .models import Book


class AddBookForm(forms.ModelForm):
	picture = forms.ImageField(required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)



	class Meta:

		model=Book
		fields=['book_name','book_writer','description','price','code_a_barre','picture','category']
		