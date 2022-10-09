from django.shortcuts import render ,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm ,UserProfileForm , UserProfileForm1 ,UserProfileChangePasswordForm
from .models import Account , UserProfile ,ReviewRationg
from django.http import HttpResponse  ,HttpResponseRedirect
from book.models import Book
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
import json
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
	if request.user.is_authenticated:
		return redirect('register1')
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
			
			#user.save()
			#profile=UserProfile()
			user=auth.authenticate(email=email,password=password)
			if user is not None:
				#message = render_to_string('accounts/account_verification_email.html',{
				#'user':user,
				#'domain':current_site,
				#'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				#'token':default_token_generator.make_token(user)
				#})
				#text=strip_tags(message)
				#to_email=email
				#send_email=EmailMultiAlternatives(f'{mail_subject}',f'{mail_subject}',EMAIL_HOST_USER,[f'{email}'])
				#send_email.attach_alternative(message,'text/html')
				#send_email.send()
				auth.login(request,user)
				return redirect('register1')

		
			
		#	response=  render (request, 'accounts/register2.html')
		#	key=bytes(b'juT0wdzMLwlKBHq2ZI1lRahYw-k6kJaP33W2mbaqScc=')
		 #	fernet = Fernet(key)
		#	message=str(user.id)
		#	encMessage = fernet.encrypt(bytes(message,'utf-8'))


#			response.set_cookie('userid',encMessage)
#			return response
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
	if request.user.is_step1 :
		return redirect('register2')



	#user_id= request.COOKIES['userid']
	 #key=bytes(b'juT0wdzMLwlKBHq2ZI1lRahYw-k6kJaP33W2mbaqScc=')
	#fernet = Fernet(key)
	#print(type(user_id))
	#print(user_id)
	#print(bytes(user_id,'utf-8'))
	#user_id=fernet.decrypt(bytes(user_id[2:-1],'utf-8'))
	_u=Account.objects.get(id=request.user.id)
	if request.method == 'POST':
		form=UserProfileForm1(request.POST)
		if form.is_valid():
			user=UserProfile.objects.get(user=_u)
			user.address_line_1=form.cleaned_data['address_line_1']
			user.address_line_2=form.cleaned_data['address_line_2']
			user.vilee=form.cleaned_data['vilee']
			user.etat=form.cleaned_data['etat']
			user.codepostal=form.cleaned_data['codepostal']
			user.save()
			_u.is_step1=True
			_u.save()
			return redirect(register2)
	else:
		form=UserProfileForm1()
	context={'form':form}



	return render (request ,'accounts/register2.html',context)
def register2(request):
	if request.user.is_step2 :
		return redirect('dashboard' ,username=(request.user.username))

	if request.method =="POST":
		form=UserProfileForm(request.POST,request.FILES)
		if form.is_valid():

		# user_id= request.COOKIES['userid']
		# key=bytes(b'juT0wdzMLwlKBHq2ZI1lRahYw-k6kJaP33W2mbaqScc=')
		# fernet = Fernet(key)
		# user_id=fernet.decrypt(bytes(user_id[2:-1],'utf-8'))
		 _u=Account.objects.get(id=request.user.id)
		 user=UserProfile.objects.get(user=_u)
		 user.profile_picture=form.cleaned_data['profile_picture']
		 user.phone_number=form.cleaned_data['phone_number']
		 user.description=form.cleaned_data['description']
		 user.instagram=form.cleaned_data['instagram']
		 user.facebook=form.cleaned_data['facebook']
		 user.whattpad=form.cleaned_data['whattpad']
		 user.goodreads=form.cleaned_data['goodreads']
		 user.save()
		 _u.is_step2=True
		 _u.save()
		 mail_subject="Please activate your account"
		 current_site=get_current_site(request)
		 message = render_to_string('accounts/account_verification_email.html',{
				'user':user,
				'domain':current_site,
				'uid':urlsafe_base64_encode(force_bytes(_u.pk)),
				'token':default_token_generator.make_token(_u)
				})
		 text=strip_tags(message)
		 to_email=_u.email
		 send_email=EmailMultiAlternatives(f'{mail_subject}',f'{mail_subject}',EMAIL_HOST_USER,[f'{to_email}'])
		 send_email.attach_alternative(message,'text/html')
		 send_email.send()

         

		 return redirect('dashboard',username=(request.user.username))
	else:
		form=UserProfileForm()

	context={
	'form':form
	}
	return render (request ,'accounts/register3.html',context)


def login (request):
	if request.user.is_authenticated:
		return redirect('dashboard',username=(request.user.username))
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
			#if user.is_admin:
			#	redirect('admin')
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
	print(default_token_generator.check_token(user,token))
	if user is not None and default_token_generator.check_token(user,token):
		user.is_verif=True
		user.save()
		messages.success(request,'Congratulation!! Your Account is activated')
		return redirect('dashboard',username=(request.user.username))
	else:
		messages.error(request,'invalid activation link')
		return redirect('register')



	return HttpResponse("ok")

@login_required(login_url ='login' )
def dashboard(request,username):
	if request.user.is_step1 == False:
		return redirect('register1')
	if request.user.is_step2 == False :
	    return redirect('register2')	
	if  request.user.is_verif == False :
		 return render(request,'accounts/verif_email.html')

	user=Account.objects.get(username=username)
	userprofile=get_object_or_404(UserProfile,user=user)
	Books=Book.objects.filter(user=user)
	paginator=Paginator(Books,5)
	page=request.GET.get('page')
	paged_books=paginator.get_page(page)
	review=ReviewRationg.objects.filter(username_add_to=username)
	print(review)
	s=0
	for i in review:
		s+=i.rating
		print(i.rating)
	if   review.count() != 0:
		s= int(s/review.count())
	else:
		s=0
	context={
    'userprofile':userprofile,
    'bookcount':Books.count(),
    'books':paged_books,
    'username':username,
    'review':review,
    's':s
    }
    

	

	return render(request,'accounts/dashboard.html',context)


def add_review(request,username):
	review=ReviewRationg()
	review.review=request.POST['reviw']
	review.rating=request.POST['rating2']
	review.ip=request.META.get('REMOTE_ADDR')
	review.username_add_to=username
	review.user=request.user
	review.save()



	
	return redirect ('dashboard',username=(username))


def forgotPassword(request):
	if request.method == 'POST':
		email = request.POST['email']
		if Account.objects.filter(email=email).exists():
			user=Account.objects.get(email__exact=email)
			#email te3 passwoard
			current_site=get_current_site(request)
			mail_subject="réinitialisez votre mot de passe "
			message = render_to_string('accounts/reset_password_email.html',{
				'user':user,
				'domain':current_site,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':default_token_generator.make_token(user)
				})
			to_email=email
			send_email=EmailMessage(mail_subject,message,to=[to_email])
			send_email.send()
			messages.success(request,'Un e-mail de réinitialisation du mot de passe a été envoyé à votre adresse e-mail ..')
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


@login_required(login_url='login')
def edit_profile_account ( request):
	x=UserProfile.objects.get(user=request.user)
	y=Account.objects.get(email=request.user.email)
	if request.method == 'POST':
		
		k=Account.objects.all()
		
		b=False
		for i in k :
			if i.username == request.POST['username']:
				b=True
		if b :
			messages.error(request,'mawjoud baba')
		else:
			if request.POST['username'] != '':
				y.username=request.POST['username']
				y.save()
				messages.success(request,'sa7ti')

        
		x.description=request.POST['description']
		if   'picture1' in request.FILES :
			print('ok')
			if request.POST['instagram'] != '': 
				x.instagram=request.POST['instagram']
			if request.POST['facebook'] != '':
				x.facebook=request.POST['facebook']
			
			if request.POST['Wattpad'] != '':
				x.whattpad=request.POST['Wattpad']

			if request.POST['goodreads']	 != '':
				x.goodreads=request.POST['goodreads']			
			if request.POST['description'] != '':
				x.description=request.POST['description']
			x.profile_picture=request.FILES['picture1']
			
			
			
			
			x.save()
			messages.success(request,'work done')
		else:
			if request.POST['description'] != '' :
				x.description=request.POST['description']			
			if request.POST['instagram'] != '':
				x.instagram=request.POST['instagram']
			if request.POST['facebook'] != '':
				x.facebook=request.POST['facebook']
			
			if request.POST['Wattpad'] != '':
				x.whattpad=request.POST['Wattpad']

			if request.POST['goodreads']	 != '':
				x.goodreads=request.POST['goodreads']	
			x.save()
			messages.success(request,'work done')


		

	context={
	'x':x,'y':y
	}

	return render (request ,'accounts/edit_profile_account.html',context)


def edit_profile_security (request):
    



	return render(request ,'accounts/edit_profile_security.html')
def edit_profile_security_password (request):
	user=Account.objects.get(username=request.user.username)
	if request.method == "POST" :
		current_password= request.POST['current_password']
		new_password=request.POST['new_password']
		verify_password=request.POST['verify_password']
		if new_password == verify_password:
			success = user.check_password(current_password)
			if success :
				user.set_password(new_password)
				user.save()
				messages.success(request,'password udated success')
			else :
				messages.error(request ,'please enter valid current password!!')
		else:
			messages.error(request,'passdoes not match')
	



	return render(request ,'accounts/edit_profile_security.html')






def edit_profile_security_email(request):
	user=Account.objects.get(username=request.user.username)
	print(request.POST)
	if request.method == "POST":
		new_email=request.POST['new_email']
		verify_email=request.POST['verify_email']
		password=request.POST['password']
		print(new_email == verify_email)

		success= user.check_password(password)
		print(success)
		print(new_email == verify_email)
		if new_email == verify_email :
			if success:
				user.email=new_email
				user.save()
				messages.success(request,'email updated succes')
			else :
				messages.error(request,'please enter valid password')
		else:
			messages.error(request,"new email dont match verify  email")





	return render( request ,'accounts/edit_profile_security.html')


def edit_profile_security_phone(request):
	user=Account.objects.get(username=request.user.username)
	if request.method == 'POST':
		new_phone=request.POST['new_phone']
		verify_phone=request.POST['verify_phone']
		password=request.POST['password']
		if new_phone == verify_phone:
			success=user.check_password(password)
			if success:
				profile=UserProfile.objects.get(user=user)
				profile.phone_number=new_phone
				profile.save()
				messages.success(request,'phone number updated succes')
			else:
				messages.error(request ,' please enter valid password')
		else:
			messages.error(request,'new phone number dont match with verify ')

	return render(request ,'accounts/edit_profile_security.html')




def edit_profile_adress(request):
	user=Account.objects.get(username=request.user.username)
	profile=UserProfile.objects.get(user=user)
	if request.method == 'POST':
		adress1=request.POST['adress1']
		adress2=request.POST['adress2']
		city=request.POST['city']
		state=request.POST['state']
		zipecode=request.POST['zipecode']
		print(request.POST)
		
		profile.address_line_1=adress1
		profile.address_line_2=adress2
		profile.vilee=city
		profile.etat=state
		profile.codepostal=zipecode
		profile.save()	

	

	return render(request ,'accounts/edit_profile_adress.html',{'profile':profile})	