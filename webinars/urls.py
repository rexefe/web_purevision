from django.urls import path, include
from .views import *



urlpatterns = [
	path('webinar/', webinar ),#fromPages
    path('webinars/',webinar_list_view),
    path('<int:id>/webinar/',webinar_detail_view),
]