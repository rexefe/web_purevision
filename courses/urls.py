from django.urls import path, include
from .views import *



urlpatterns = [
	path('search/', SearchResultsView, name='search_results'),
	path('<int:id>/category', course_list_view),
	path('<int:id>/course', course_detail_view, name='course_detail'),
	path('<int:id>/test', test_course_detail_view, name='test_course_detail'),
	path('your-courses/', mycourse_view, name='mycourse_view'),
	path('course/register/', register_course, name='register_course'),

]

