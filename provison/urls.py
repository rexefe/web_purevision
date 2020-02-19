
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 



urlpatterns = [
	#Main pages
    path('admin/', admin.site.urls),
    path('', include('pages.urls'), name='page'),
    path('', include('provison_users.urls')),
    path('', include('webinars.urls')),
    path('', include('courses.urls'), name='courses'),
     path('', include('inmessages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)