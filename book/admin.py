from django.contrib import admin
from .models import Book ,bookgallery
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display=('book_name','price','category','modified_date','is_available')


admin.site.register(Book,BookAdmin)
admin.site.register(bookgallery)