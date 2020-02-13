from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pprint import pprint
#from courses.models import *

class Profile(models.Model):

    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    

  
    TYPE = (
        ('Company', 'Company'),
        ('Individual', 'Individual'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    pobox = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    user_type = models.CharField(choices=TYPE, default='Individual', max_length=10, blank=True)
    bio = models.TextField(null=True, max_length=850)
    signup_confirmation = models.BooleanField(default=False)
    #course_id = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(instance)
        print('Printed this objects')
        instance.profile.save()

class Participant(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    first_name =  models.CharField(max_length=200, null=True, blank=True)
    last_name =  models.CharField(max_length=200, null=True, blank=True)
    job_title =  models.CharField(max_length=200, null=True, blank=True)
    email =  models.CharField(max_length=200, null=True, blank=True)