from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class InHouseProposal(models.Model):

	class Days(models.IntegerChoices):
		ONE = 1
		TWO = 2
		THREE = 3
		FOUR = 4
		FIVE = 5

	LEVEL = [('Senior Management','Senior Management'),
			('Middle Management','Middle Management'),
			('First Line Supervisory','First Line Supervisory'),
			('Administration/Non-Supervisory','Administration/Non-Supervisory'),
			('Mixed','Mixed')]

	name = models.CharField(max_length=200, null=False, blank=False)
	location = models.CharField(max_length=200, null=False, blank=False)
	days = models.IntegerField(choices=Days.choices, null=False, blank=False, default=1)
	participants = models.IntegerField(null=False, blank=False)
	language = models.CharField(max_length=200, null=False, blank=False)
	level = models.CharField(max_length=200, choices= LEVEL, null=False, blank=False)
	requirements = models.TextField(max_length=1000)

	#quick contact info
	first_name =  models.CharField(max_length=200, null=False, blank=False)
	last_name =  models.CharField(max_length=200, null=False, blank=False)
	job_title =  models.CharField(max_length=200, null=False, blank=False)
	phone  =  models.CharField(max_length=200, null=False, blank=False)
	address  =  models.CharField(max_length=200)
	email = models.CharField(max_length=200, null=False, blank=False)
	pobox = models.CharField(max_length=200)
	city = models.CharField(max_length=200, null=False, blank=False)
	company = models.CharField(max_length=200, null=False, blank=False)
	country = models.CharField(max_length=200, null=False, blank=False)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + '|' + self.name





