from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm ,UserProfileForm , UserProfileForm1
from .models import Account , UserProfile
from django.http import HttpResponse  
from book.models import Book
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
import json
from cryptography.fernet import Fernet

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage ,EmailMultiAlternatives
from Biblichor.settings import EMAIL_HOST_USER
def register (request):
	x=""
	if request.method == 'POST':
		form =RegistrationForm(request.POST)
		if form.is_valid():
			
			first_name= form.cleaned_data['first_name']
			last_name= form.cleaned_data['last_name']
			username= form.cleaned_data['username']
			email= form.cleaned_data['email']
			password= form.cleaned_data['password']
			
			user =Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
			user.save()
			profile=UserProfile()
			
			profile.user=user
			profile.save()			
			mail_subject="Please activate your account"
			current_site=get_current_site(request)
			message = render_to_string('accounts/account_verification_email.html',{
				'user':user,
				'domain':current_site,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':default_token_generator.make_token(user)
				})
			text=strip_tags(message)
			to_email=email
			send_email=EmailMultiAlternatives(f'{mail_subject}',f'{mail_subject}',EMAIL_HOST_USER,[f'{email}'])
			send_email.attach_alternative(message,'text/html')
			send_email.send()
			user.save()
			profile=UserProfile()

		
			
			response=  render (request, 'accounts/register2.html')
			key=bytes(b'juT0wdzMLwlKBHq2ZI1lRahYw-k6kJaP33W2mbaqScc=')
			fernet = Fernet(key)
			message=str(user.id)
			encMessage = fernet.encrypt(bytes(message,'utf-8'))


			response.set_cookie('userid',encMessage)
			return response
		else:
			x=form.errors.as_json()
			x=x
			t=json.loads(x)
			x=t[list(t)[0]][0]['message']
			print(x)
			

	else :

		form=RegistrationForm()

	context={'form':form ,'test':x}



	return render(request ,'accounts/register1.html',context)

def register1(request):

	user_id= request.COOKIES['userid']
	key=bytes(b'juT0wdzMLwlKBHq2ZI1lRahYw-k6kJaP33W2mbaqScc=')
	fernet = Fernet(key)
	print(type(user_id))
	print(user_id)
	print(bytes(user_id,'utf-8'))
	user_id=fernet.decrypt(bytes(user_id[2:-1],'utf-8'))
	_u=Account.objects.get(id=user_id)
	if request.method == 'POST':
		form=UserProfileForm1(request.POST)
		if form.is_valid():
			user=UserProfile.objects.get(user=_u)
			user.address_line_1=form.cleaned_data['address_line_1']
			user.address_line_2=form.cleaned_data['address_line_2']
			user.vilee=request.form.cleaned_data['vilee']
			user.etat=request.form.cleaned_data['etat']
			user.codepostal=form.cleaned_data['codepostal']
			user.save()
			return redirect(register2)
	else:
		form=UserProfileForm1(request.POST)
	context={'form':form}



	return render (request ,'accounts/register2.html',context)
def register2(request):
	if request.method =="POST":
		form=UserProfileForm(request.POST)
		if form.is_valid():

		 user_id= request.COOKIES['userid']
		 key=bytes(b'juT0wdzMLwlKBHq2ZI1lRahYw-k6kJaP33W2mbaqScc=')
		 fernet = Fernet(key)
		 user_id=fernet.decrypt(bytes(user_id[2:-1],'utf-8'))
		 _u=Account.objects.get(id=user_id)
		 user=UserProfile.objects.get(user=_u)
		 user.phone_number=form.cleaned_data['phone_number']
		 user.description=form.cleaned_data['description']
		 user.instagram=form.cleaned_data['instagram']
		 user.facebook=form.cleaned_data['facebook']
		 user.whattpad=form.cleaned_data['whattpad']
		 user.goodreads=form.cleaned_data['goodreads']
		 user.save()




		 return redirect(login)
	else:
		form=UserProfileForm()

	context={
	'form':form
	}
	return render (request ,'accounts/register3.html',context)


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
			return render(request ,'under.html')
		else:
			messages.error(request,'E-mail ou Mot de passe incorrect')
			return redirect ('login')
	return render(request ,'accounts/login.html')




@login_required(login_url ='login' )
def logout (request):

	auth.logout(request)
	messages.success(request,'You are logged out')

	return redirect('login')

def activate (request,uidb64,token):
	try:

		uid=urlsafe_base64_decode(uidb64).decode()
		user=Account._default_manager.get(pk=uid)
	except(TypeError,valueError,OverflowError,Account.DoesNotExist):
		user=None

	if user is not None and default_token_generator.check_token(user,token):
		user.is_active=True
		user.save()
		messages.success(request,'Congratulation!! Your Account is activated')
		return redirect('login')
	else:
		messages.error(request,'invalid activation link')
		return redirect('register')



	return HttpResponse("ok")

@login_required(login_url ='login' )
def dashboard(request):
	userprofile=get_object_or_404(UserProfile,user=request.user)
	Books=Book.objects.filter(user=request.user)
	context={
    'userprofile':userprofile,
    'bookcount':Books.count(),
    'books':Books
    }
    

	

	return render(request,'accounts/dashboard.html',context)




def forgotPassword(request):
	if request.method == 'POST':
		email = request.POST['email']
		if Account.objects.filter(email=email).exists():
			user=Account.objects.get(email__exact=email)
			#email te3 passwoard
			current_site=get_current_site(request)
			mail_subject="Reset your password "
			message = render_to_string('accounts/reset_password_email.html',{
				'user':user,
				'domain':current_site,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':default_token_generator.make_token(user)
				})
			to_email=email
			send_email=EmailMessage(mail_subject,message,to=[to_email])
			send_email.send()
			messages.success(request,'Password reset email has ben sent to your email address ..')
			return redirect('login')

		else:
			messages.error(request,"Ce compte n'existe pas.")
			return redirect('forgotPassword')

	return  render( request,'accounts/forgotPassword.html')


def resetpassword_validate (request,uidb64,token):
	try:

		uid=urlsafe_base64_decode(uidb64).decode()
		user=Account._default_manager.get(pk=uid)
	except(TypeError,valueError,OverflowError,Account.DoesNotExist):
		user=None
	if user is not None and default_token_generator.check_token(user,token):
		request.session['uid']=uid
		messages.success(request ,'please reset your password')
		return redirect('resetPassword')
	else:
		messages.error(request,'This link has been expired!')
		return redirect('login')




def resetPassword(request):
	if request.method == 'POST':
		password =request.POST['Password']
		confirm_password=request.POST['confirm_password']

		if confirm_password == password:
			uid=request.session.get('uid')
			user=Account.objects.get(pk=uid)
			user.set_password(password)
			user.save()
			messages.success(request,'Mot de passe modifié avec succès')
			return redirect ('login')
		else:
			messages.error(request,' Mot de passes non compatibles ')
			return render(request,'accounts/resetPassword.html')
	else:
		return render(request , 'accounts/resetPassword.html')