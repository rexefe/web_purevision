from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Authur(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	profile_picture = models.ImageField(upload_to='instructors/', default='/images/test1.jpg')
	name = models.CharField(max_length=150)
	role = models.CharField(max_length=150, null=True)
	description = models.TextField(null=True)
	facebook = models.CharField(max_length=150, default='www.facebook.com')
	twitter = models.CharField(max_length=150, default='www.twitter.com')
	linkedin = models.CharField(max_length=150, default='www.linkedin.com')
	display = models.BooleanField(default=False)



	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Instructors'




