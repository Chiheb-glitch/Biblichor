from django import forms 
from .models import Book


class AddBookForm(forms.ModelForm):
	picture = forms.ImageField(required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)



	class Meta:

		model=Book
		fields=['book_name','book_writer','description','price','code_a_barre','picture','category','quantity']
	def __init__(self,*args,**kwargs):
			super(AddBookForm, self).__init__(*args,**kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs['class'] = 'form-control'
				self.fields[field].widget.attrs['id'] = 'text-input'
			self.fields['book_name'].widget.attrs["Placeholder"]="Titre"
			self.fields['book_writer'].widget.attrs["Placeholder"]="Auteur"
			self.fields['description'].widget.attrs["Placeholder"]="description"
			self.fields['picture'].widget.attrs["onchange"]="loadFile1(event,'1')"
			self.fields['quantity'].widget.attrs["Placeholder"]="quantity"
			self.fields['price'].widget.attrs["Placeholder"]="price"
			self.fields['category'].widget.attrs["class"]=""
		