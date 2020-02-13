from django.urls import path, include
from .views import *



urlpatterns = [
	path('', home, name ='home' ),
	path('blended-learning', service_blended_learning ),
    path('consultancy-services', consultancy_services ),
    path('e-learning-solutions', e_learning_solutions ),
    path('empowerment-leadership-program-elp', empowerment_leadership_program_elp ),
    path('engineering-management-consulting', engineering_management_consulting ),
    path('executive-coaching', executive_coaching ),
    path('in-house-courses', in_house_courses ),
    path('individual-training-program-itp', individual_training_program_itp ),
    path('intelligent-leader-program-ilp5', intelligent_leader_program_ilp5 ),
    path('iso-robot', iso_robot ),
    path('outsourcing-solutions', outsourcing_solutions ),
    path('talent-tool', talent_tool ),
    path('testing-examination-center', testing_examination_center ),

    #About Us
	path('aboutus', aboutus ),
	path('accreditations', accreditations ),
	path('clients', clients ),
	path('contactus', conatctus ),
	path('instructors', instructors ),
]