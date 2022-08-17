
from django.shortcuts import render,redirect, get_object_or_404
from book.models import Book
from .models import CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.



'''def cart (request):
	if request.user.is_authenticated:
		cart_items=CartItem.objects.filter(user=request.user)
	else:
	    cart_items=False
	return dict(cart_items=cart_items) 

'''
login_required(login_url='login')
def add_cart(request,code_a_barre):
	book=Book.objects.get(code_a_barre=code_a_barre)
	cartitem=CartItem()
	cartitem.book=book
	cartitem.user=request.user
	cartitem.save()
	return redirect('book_detail',category_slug=(book.category.slug),code_a_barre=(code_a_barre))


