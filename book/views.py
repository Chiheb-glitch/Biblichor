from django.shortcuts import render,redirect
from .models import Book
from .forms import AddBookForm
# Create your views here.
def store (request):
	books= Book.objects.all().filter(is_available=True)
	book_count=books.count()



	context = {
	'books':books,
	'count':book_count
	}
	return  render (request , 'store/store.html', context)





def Add_book(request):

	if request.method == "POST":
		form= AddBookForm(request.POST,request.FILES)
		if form.is_valid():
			book_name=form.cleaned_data['book_name']
			book_writer=form.cleaned_data['book_writer']
			description=form.cleaned_data['description']
			price=form.cleaned_data['price']
			code_a_barre=form.cleaned_data['code_a_barre']
			#image=form.cleaned_data['picture']
			category=form.cleaned_data['category']

			#b=Book()
			#b.book_name=book_name
			#b.book_writer=book_writer
			#b.description=description
			#b.price=price
			#b.code_a_barre=code_a_barre
			#b.image=request.FILES['file']
			#b.category=category
			#b.save()
			#print(book_name)
			form.save(commit=True)
			return redirect('store')
	else:
		form=AddBookForm()


	context={'form':form}




	return render(request ,'store/addbook.html' , context)


