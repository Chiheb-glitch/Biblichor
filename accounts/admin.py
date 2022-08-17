from django.contrib import admin
from .models import Account , UserProfile ,ReviewRationg
from django.utils.html import format_html
from django.contrib.auth.admin  import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display =('email','first_name','last_name','last_login','date_joined','is_active')
	liest_display_links=('email','first_name','last_name')
	readonly_fields=('last_login','date_joined')
	#ordering=('-date_joined',_)

	filter_horizontal=()
	list_filter=()
	fieldsets=()


#class UserProfileAdmin(admin.ModelAdmin):

	#def thumbnail (self,object):
		#return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
	#thumbnail.short_description='profile picture'


	#list_display=('thumbnail' ,'user','city','state')
	#list_display=('user','city','state')
#admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile)
admin.site.register(ReviewRationg)
