from .models import  CartItem


def Cart_context (request):
	if request.user.is_authenticated:
		cart_items=CartItem.objects.filter(user=request.user)
		list_code=[]
		for x in cart_items:
			list_code.append(x.book.code_a_barre)
	    
	else:
	    cart_items=False
	    list_code=[]
	return dict(cart_items=cart_items,list_code=list_code) 