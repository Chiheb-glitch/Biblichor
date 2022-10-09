from django import forms 
from .models import Account,UserProfile,ChangepasswordModel



class RegistrationForm(forms.ModelForm):
	
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'Placeholder':'Mot de passe'
		}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
		'Placeholder':'vérifier le mot de passe'
		}))


	class Meta:

		model=Account
		fields=['first_name','last_name', 'username','email','password']
	def __init__(self,*args,**kwargs):
		super(RegistrationForm, self).__init__(*args,**kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs["Placeholder"]="Prénom"
		self.fields['last_name'].widget.attrs["Placeholder"]="Nom de famille"
		self.fields['username'].widget.attrs["Placeholder"]="Nom d'utilisateur"
		self.fields['email'].widget.attrs["Placeholder"]="Adresse e-mail"
	
	
    

	def clean(self):
		clean_data=super(RegistrationForm,self).clean()
		password = clean_data.get('password')
		confirm_password=clean_data.get('confirm_password')

		if password  != confirm_password :

			raise forms.ValidationError(
				'Mot de passes non compatibles',code="20"
				)
class UserProfileForm(forms.ModelForm):
	profile_picture = forms.ImageField(required=False, error_messages={'invalid':("Image files only")}, widget=forms.FileInput)
	class Meta:
		model= UserProfile
		fields=('profile_picture','phone_number','description','instagram','facebook','whattpad','goodreads')
	def __init__(self,*args,**kwargs):
			super(UserProfileForm, self).__init__(*args,**kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields['phone_number'].widget.attrs["Placeholder"]="Numéro de téléphone"
			self.fields['description'].widget.attrs["Placeholder"]="La description"
			self.fields['instagram'].widget.attrs["Placeholder"]="Lien Instagram"
			self.fields['facebook'].widget.attrs["Placeholder"]=" Lien Facebook "
			self.fields['whattpad'].widget.attrs["Placeholder"]=" Lien Whattpad "
			self.fields['goodreads'].widget.attrs["Placeholder"]=" Lien Goodreads "
			self.fields['profile_picture'].widget.attrs["onchange"]="loadFile(event)"
			self.fields['profile_picture'].widget.attrs["id"]="file"
			self.fields['phone_number'].required=True





class UserProfileForm1(forms.ModelForm):
	class Meta:
		model= UserProfile
		fields=('address_line_1','address_line_2','vilee','etat','codepostal')
	def __init__(self,*args,**kwargs):
			super(UserProfileForm1, self).__init__(*args,**kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields['address_line_1'].widget.attrs["Placeholder"]="Adress 1"
			self.fields['address_line_2'].widget.attrs["Placeholder"]="Adress 2"
			self.fields['vilee'].widget.attrs["Placeholder"]="Ville"
			self.fields['etat'].widget.attrs["Placeholder"]=" Etat "
			self.fields['codepostal'].widget.attrs["Placeholder"]="Code postal"
			self.fields['address_line_2'].required=False


class UserProfileChangePasswordForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(attrs={
		'Placeholder':'Mot de passe'
		}))
	verif_password=forms.PasswordInput()
	class Meta:
		model=ChangepasswordModel
		fields=('password','verify_password')

	
	#def __init__(self,*args,**kwargs):
	def clean(self):
		clean_data=super(RegistrationForm,self).clean()
		password = clean_data.get('password')
		verify_password=clean_data.get('verify_password')

		if password  != confirm_password :

			raise forms.ValidationError(
				'Mot de passes non compatibles',code="20"
				)
		