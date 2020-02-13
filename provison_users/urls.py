from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
	path('accounts/login/', login_view, name="login_view"),
    path('accounts/signup/', signup_view, name="signup_view"),
    path('accounts/logout/', logout_view, name="logout_view"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('profile/', profile_view, name="profile_view"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='provison_users/password_reset.htm'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='provison_users/password_reset_done.htm'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='provison_users/password_reset_confirm.htm'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='provison_users/password_reset_complete.htm'
         ),
         name='password_reset_complete'),

    path('accounts/password-change/',auth_views.PasswordChangeView.as_view(
    	template_name='provison_users/password_change_form.htm'), name="password_change"),
    path('accounts/password-change/done/', auth_views.PasswordChangeDoneView.as_view(
    	template_name='provison_users/password_change_done.htm'), name="password_change_done"),


]