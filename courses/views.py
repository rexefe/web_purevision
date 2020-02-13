from django.shortcuts import render, get_object_or_404
from .models import Course, Category, CourseInfo, MyCourse, Location, Language
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.db.models import Q
# Create your views here.


def SearchResultsView(request): # new
	category = Category.objects.all()
	cities = Location.objects.all()
	language = Language.objects.all()

	if True:
		query = []
		query.append(request.GET.get('q'))
		if query[0]:
			query.append(request.GET.get('category_id'))
			query.append(request.GET.get('city_id'))
			query.append(request.GET.get('lang_id'))
			query.append(request.GET.get('month'))
			query.append(request.GET.get('year'))
			'''& Q(course_id__category=query[1])
					  | Q(location=query[2]) | Q(language=query[3])
					   | Q(start_date__year=query[5])
					   '''
			object_list = CourseInfo.objects.filter(
					Q(course_id__title__icontains=query[0])  

			)

			course_list = []
			for items in object_list:

				if items.course_id in course_list:
					continue
				else:
					course_list.append(Course.objects.get(pk=items.course_id.id))

			print(type(object_list))

			context = { "course_list": course_list,
						'categories': category,
    		  			'cities': cities,
    		   			'languages': language, }

			return render(request, "courses/course_search_results.htm", context)

			


#| Q(state__icontains=query)
        
def course_list_view(request, id):
	#A VERY DYNAMIC VIEW
	#all the categories printed
	categories = Category.objects.all()

	#the One category to print
	category = Category.objects.get(pk=id)

	#Filter all the course for the category
	courses = Course.objects.filter(category=category)
	

	context = {'courses': courses, 'categories':categories, 'category':category}

	return render(request, "courses/courses.htm", context)

def course_detail_view(request, id):
	#Call all thee Categories
	categories = Category.objects.all()
	obj = get_object_or_404(Course, id=id)
	context = {
        "object": obj,
        'categories': categories
	}

	return render(request, "courses/course_detail.htm", context)


@login_required
def mycourse_view(request):
	courses = MyCourse.objects.filter(user_id=request.user.id)

	context = {"courses": courses}
	return render(request, 'courses/mycourses.htm', context)

def test_course_detail_view(request, id):
	#Call all thee Categories
	categories = Category.objects.all()
	obj = get_object_or_404(Course, id=id)
	context = {
        "course": obj,
        'categories': categories
	}

	return render(request, "courses/test_course_detail.htm", context)


def register_course(request):

	query = request.GET.get('q')
	course = get_object_or_404(CourseInfo, id=query)

	print(course)
	categories = Category.objects.all()
	print(categories)

	context = {'course':course,
				'categories':categories}

	return render(request, "courses/registration-form.htm", context)


#Def Done










