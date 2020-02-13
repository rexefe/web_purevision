from django.contrib.auth import (
	login, 
	logout,
	authenticate,
	get_user_model,

)
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string

from .forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


def activation_sent_view(request):
		return render(request, 'provison_users/activation_sent.htm')

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
    # checking if the user exists, if the token is valid.
	if user is not None and account_activation_token.check_token(user, token):
		# if valid set active true 
		user.is_active = True
		# set signup_confirmation true
		user.profile.signup_confirmation = True
		user.save()
		user.profile.save()
		print(user.profile.signup_confirmation)
		print('Check if this thing printed')

		login(request, user)
		return redirect('home')
	else:
		return render(request, 'provison_users/activation_invalid.htm')

def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)

		return redirect('/')  
	context = {'form': form }

	return render(request, "provison_users/login.htm", context)


def signup_view(request):
	next = request.GET.get('next')
	form = UserRegistrationForm(request.POST or None)
	#form = UserRegistrationForm(request.POST)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user.set_password(password)
		
		user.is_active = False
		user.save()
		
		

		current_site = get_current_site(request)
		subject = 'Please Activate Your Account'
		# load a template like get_template() 
		# and calls its render() method immediately.

		email_from = settings.EMAIL_HOST_USER    #OurEmail
		recipient = []
		recipient.append(form.cleaned_data.get('email')) #useremail

		message = render_to_string('provison_users/activation_request.htm', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				# method will generate a hash value with user related data
				'token': account_activation_token.make_token(user),
				})

		send_mail( subject, message, email_from, recipient )

		#user.email_user(subject, message)

		return redirect('activation_sent')
		
	context = {'form': form}	

	return render(request, 'provison_users/signup.htm', context)

def logout_view(request):
	logout(request)
	return redirect('/')

@login_required
def profile_view(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
 		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'provison_users/profile.htm', context)

def email(request):
	subject = 'Thank you for registering to our site'
	message = ' it  means a world to us '
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ['rexefe@outlook.com'] 
	send_mail( subject, message, email_from, recipient_list )
	return render(request, 'provison_users/profile.htm', {})