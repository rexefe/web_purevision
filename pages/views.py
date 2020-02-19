from django.shortcuts import render
from courses.models import Course, Category, Location, Language
from aurthor.models import Authur
#main pages

#my changes
def testcat(request):
	return render(request, 'category.htm', {})

def home(request):
	#courses = Course.objects.filter(date__year='2020')
	special_courses = Course.objects.filter(event='Special')[:6]
	upcoming_courses = Course.objects.filter(event='Upcoming')[:6]
	category = Category.objects.all()
	cities = Location.objects.all()
	language = Language.objects.all()
	aurthor = Authur.objects.all()

	print(aurthor)

	context = {'special_courses': special_courses,
				'upcoming_courses': upcoming_courses,
				'categories': category,
				'cities': cities,
				 'languages': language, 
				 'aurthor':aurthor}
    
	return render(request, 'home.htm', context)

#Services
def service_blended_learning(request, *args, **kwargs):
	return render(request, 'Services/blended_learning.htm', {})

def consultancy_services(request, *args, **kwargs):
	return render(request, 'Services/consultancy-services.htm', {})

def e_learning_solutions(request, *args, **kwargs):
	return render(request, 'Services/e-learning-solutions.htm', {})

def empowerment_leadership_program_elp(request, *args, **kwargs):
	return render(request, 'Services/empowerment-leadership-program-elp.htm', {})

def engineering_management_consulting(request, *args, **kwargs):
	return render(request, 'Services/engineering-management-consulting.htm', {})

def executive_coaching(request, *args, **kwargs):
	return render(request, 'Services/executive-coaching.htm', {})

def in_house_courses(request, *args, **kwargs):
	return render(request, 'Services/in-house-courses.htm', {})

def individual_training_program_itp(request, *args, **kwargs):
	return render(request, 'Services/individual-training-program-itp.htm', {})

def intelligent_leader_program_ilp5(request, *args, **kwargs):
	return render(request, 'Services/intelligent-leader-program-ilp5.htm', {})

def iso_robot(request, *args, **kwargs):
	return render(request, 'Services/iso-robot.htm', {})

def outsourcing_solutions(request, *args, **kwargs):
	return render(request, 'Services/outsourcing-solutions.htm', {})

def talent_tool(request, *args, **kwargs):
	return render(request, 'Services/talent-tool.htm', {})

def testing_examination_center(request, *args, **kwargs):
	return render(request, 'Services/testing-examination-center.htm', {})

#Aboutus
def aboutus(request, *args, **kwargs):
	return render(request, 'about/aboutus.htm', {})

def accreditations(request, *args, **kwargs):
	return render(request, 'about/accreditations.htm', {})

def clients(request, *args, **kwargs):
	return render(request, 'about/clients.htm', {})

def conatctus(request, *args, **kwargs):
	return render(request, 'about/contactus.htm', {})

def instructors(request, *args, **kwargs):
	return render(request, 'about/instructors.htm', {})






	
	
