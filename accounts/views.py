from django.shortcuts import render ,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm 
from .models import Account , UserProfile

# Create your views here.


def register (request):
	if request.method == 'POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			first_name= form.cleaned_data['first_name']
			last_name= form.cleaned_data['last_name']
			phone_number= form.cleaned_data['phone_number']
			email= form.cleaned_data['email']
			password= form.cleaned_data['password']
			username=email.split("@")[0]


			user =Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
			user.phone_number = phone_number
			user.save()
			profile=UserProfile()
			profile.user=user
			profile.save()
			return redirect(dashboard)
	else :
		form=RegistrationForm()
	context={'form':form ,
		}



	return render(request ,'accounts/register1.html',context)

def register1(request):
	return render (request ,'accounts/register2.html')
def register2(request):
	return render (request ,'accounts/register3.html')


def login (request):
	print(request)
	if request.method=='POST':
		print("firsttttt")
		email=request.POST['email']
		password=request.POST['password']
		print(email)
		print(password)
		user=auth.authenticate(email=email,password=password)
		print(user)
		if user is not None:
			auth.login(request,user)
			print('defffffffffff')
			return redirect ('dashboard')
		else:
			return redirect ('login')
	return render(request ,'accounts/login.html')




@login_required(login_url ='login' )
def logout (request):

	auth.logout(request)
	messages.success(request,'You are logged out')
	return redirect('login')



@login_required(login_url ='login' )
def dashboard(request):


	

	return render(request,'accounts/dashboard.html')