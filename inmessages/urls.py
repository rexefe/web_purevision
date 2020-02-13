from django.urls import path, include
from .views import *



urlpatterns = [
	path('request-in-house-proposal/', request_in_house_proposal, name='request_in_house_proposal'),
	path('proposal-sent/', sent_success, name='sent_success'),
	
	
]