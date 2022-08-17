from django.db import models
from book.models import Book
from accounts.models import Account

# Create your models here.



class CartItem(models.Model):
	user = models.ForeignKey(Account , on_delete=models.CASCADE,null=True)
	book=models.ForeignKey(Book,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	is_active=models.BooleanField(default=True)


	def __str__(self):
		return self.book.book_name
