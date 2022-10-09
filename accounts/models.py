from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
	def create_user(self,first_name,last_name,username,email,password=None):
	 if not email:
	 	raise ValueError('User must have an email address ')

	 if not username:
			raise ValueError ('User must have an username')

	 user = self.model(
		email =self.normalize_email(email),
		username=username,
		first_name=first_name,
		last_name=last_name,

		)
	 user.set_password(password)
	 user.save(using=self._db)
	 return user
	def create_superuser(self,first_name,last_name,username,email,password):
		user=self.create_user(
			email=self.normalize_email(email),
			username=username,
			password=password,
			first_name=first_name,
			last_name=last_name,

			)

		user.is_admin=True
		user.is_active=True
		user.is_staff=True
		user.is_superadmin=True
		user.save(using=self._db)
		return user

  




class Account (AbstractBaseUser):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	username=models.CharField(max_length=50,unique=True, error_messages={'invalid':"you custom error message"})
	email=models.EmailField(max_length=100,unique=True)



	date_joined=models.DateTimeField(auto_now_add=True)
	last_login=models.DateTimeField(auto_now_add=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_verif=models.BooleanField(default=False)
	is_step1=models.BooleanField(default=False)
	is_step2=models.BooleanField(default=False)
	is_superadmin = models.BooleanField(default=False)

	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['username','first_name','last_name']
	objects=MyAccountManager()



	def __str__(self):
		return self.email 

	def has_perm(self , perm, obj=None):

		return self.is_admin
	def has_module_perms(self , add_label):
		return True



class UserProfile(models.Model):
	user  = models.OneToOneField(Account,on_delete=models.CASCADE)

	address_line_1=models.CharField(max_length=100,blank=False)
	address_line_2=models.CharField(max_length=100)
	profile_picture=models.ImageField(blank=True,upload_to='userprofile',default='userprofile/mainone.jfif')
	vilee=models.CharField(blank=False, max_length=20)
	etat=models.CharField(blank=False, max_length=20)
	codepostal=models.CharField(blank=False, max_length=20)
	phone_number = models.CharField(max_length=50,blank=True)
	description=models.CharField(blank=True,max_length=1500)
	instagram=models.CharField(blank=True,max_length=100)
	facebook=models.CharField(blank=True,max_length=100)
	whattpad=models.CharField(blank=True,max_length=100)
	goodreads=models.CharField(blank=True,max_length=100)
	REQUIRED_FIELDS=['address_line_1','vilee','etat']

    



	def __str__(self):
		return self.user.first_name


	def full_address(self):

		return f'{self.address_line_1} {self.address_line_2}'



class ReviewRationg(models.Model):
	user=models.ForeignKey(Account,on_delete=models.CASCADE)
	review=models.TextField(max_length=500,blank=True)
	rating=models.FloatField()
	ip=models.CharField(max_length=20,blank=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	username_add_to=models.CharField(max_length=50,blank=False,default="none")
	def __str__(self):
		return self.user.username


class ChangepasswordModel(models.Model):
	password=models.CharField(max_length=100)
	verify_password=models.CharField(max_length=100)
	