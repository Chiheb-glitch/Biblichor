from django.db import models

# Create your models here.
from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account


class Book(models.Model):
	user = models.ForeignKey(Account , on_delete=models.CASCADE,null=True)
	book_name=models.CharField(max_length=200,unique=True)
	book_writer=models.CharField(max_length=200,unique=True)
	description=models.TextField(max_length=500,blank=True)
	price =models.FloatField()
	code_a_barre =models.IntegerField()
	picture = models.ImageField(upload_to='photos/products')
	is_available=models.BooleanField(default=True)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	created_date=models.DateTimeField(auto_now_add=True)
	quantity=models.IntegerField(default="1")
	modified_date=models.DateTimeField(auto_now=True)
	pickup=models.BooleanField(default=False)
	delivery=models.BooleanField(default=False)

	

	def get_url(self):
		return reverse('book_detail',args=[self.category.slug,self.code_a_barre])




	def __str__(self):
		return self.book_name

class bookgallery(models.Model):
	book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
	image=models.ImageField(upload_to='photos/products/gallery')


	def __str__(self):
		return self.book.book_name
