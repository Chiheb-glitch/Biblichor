from django.shortcuts import render,redirect
from .models import Book ,bookgallery
from .forms import AddBookForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q 
from accounts.models import UserProfile

# Create your views here.
def store (request):
	books= Book.objects.all().filter(is_available=True)
	paginator=Paginator(books,4)
	page=request.GET.get('page')
	paged_books=paginator.get_page(page)
	book_count=books.count()




	context = {
	'books':paged_books,
	'count':book_count
	}
	return  render (request , 'store/store.html', context)



def search(request):
	if "keyword" in request.GET:
		keyword=request.GET['keyword']
		if keyword:
			books=Book.objects.order_by('-created_date').filter(Q(description__icontains= keyword) | Q(book_name__icontains=keyword))
			book_count=books.count()
			paginator=Paginator(books,8)
			page=request.GET.get('page')
			paged_books=paginator.get_page(page)

	context={
	'books':paged_books,
	'count':book_count
	}

	return render(request ,'store/store.html',context)


def filter (request):

	print(request.GET)
	books=Book.objects.all().filter(is_available=True,pickup= 'Pickup'  in request.GET ,delivery='Delivery'  in request.GET )
	book_count=books.count()
	paginator=Paginator(books,8)
	page=request.GET.get('page')
	paged_books=paginator.get_page(page)



	context={
	'books':paged_books,
	'count':book_count
	}


	return render(request ,'store/store.html',context)








def Add_book(request):

	if request.method == "POST":
		form= AddBookForm(request.POST,request.FILES)

		print('pickup1' in request.POST)
		print(request.POST)


		

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
			book=Book.objects.get(code_a_barre=code_a_barre)
			book.user=request.user
			book.pickup='pickup1' in request.POST
			book.delivery='pickup2' in request.POST
			book.save()
			for x in  request.FILES.getlist('images') :
				g=bookgallery.objects.create(
				book=book,
				image=x)
				g.save()
				print(x)
			return redirect('store')
	else:
		form=AddBookForm()


	context={'form':form}




	return render(request ,'store/test.html' , context)


def book_detail (request , category_slug , code_a_barre):

	try:
		single_book= Book.objects.get(category__slug=category_slug ,code_a_barre=code_a_barre)
		profile=UserProfile.objects.get(user=single_book.user)
		gallery=bookgallery.objects.filter(book=single_book)


	except Exception as e:
		raise e 
	context ={
	'single_book':single_book,'gallery':gallery,'profile':profile,
	}

	return render (request , 'store/book_detail.html', context)