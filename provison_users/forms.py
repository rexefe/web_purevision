from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model

)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	


	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('This users does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')
			if not user.is_active:
				raise forms.ValidationError('This user is not active')
		return super(UserLoginForm, self).clean(*args, **kwargs)		


class UserRegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(label='Email Address')
	email2 = forms.EmailField(label='Confirm Email Address')
	first_name = forms.CharField(max_length=100,)
	last_name = forms.CharField(max_length=100,)
	
	

	class Meta:
		model = User
		fields = [	'username', 'first_name', 'last_name',
					'email',
					'email2',
					'password1', 'password2' 
					]

	def clean(self):
		cleaned_data = super().clean()
		username = self.cleaned_data.get('username')
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')

		if User.objects.filter(username=username):
			raise forms.ValidationError("Username Already Exist", )

		if email != email2:
			print(email)
			print(email2)
			raise forms.ValidationError("emails must match")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email is already being used")	
			#return email

		

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = ['job', 'phone', 'company', 'address', 'pobox', 'city',
					'country', 'bio' ]



