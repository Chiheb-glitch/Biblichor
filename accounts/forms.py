from django import forms 
from .models import Account,UserProfile



class RegistrationForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'Placeholder':'Enter Password'
		}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
		'Placeholder':'Confirm Password'
		}))


	class Meta:

		model=Account
		fields=['first_name','last_name','phone_number','email','password']
	def __init__(self,*args,**kwargs):
		super(RegistrationForm, self).__init__(*args,**kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


	def clean(self):
		clean_data=super(RegistrationForm,self).clean()
		password = clean_data.get('password')
		confirm_password=clean_data.get('confirm_password')

		if password  != confirm_password :
			raise forms.ValidationError(
				'password does not match !!!!!!!!!!!'
				)
