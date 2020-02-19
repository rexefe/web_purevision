from django.urls import path, include
from .views import *



urlpatterns = [
	path('', home, name ='home' ),
    path('testcat', testcat, name ='testcat' ),
	path('blended-learning', service_blended_learning, name='service_blended_learning' ),
    path('consultancy-services', consultancy_services , name='consultancy_services'),
    path('e-learning-solutions', e_learning_solutions, name = 'e_learning_solutions' ),
    path('empowerment-leadership-program-elp', empowerment_leadership_program_elp, name='empowerment_leadership_program_elp' ),
    path('engineering-management-consulting', engineering_management_consulting, name='engineering_management_consulting' ),
    path('executive-coaching', executive_coaching, name = 'executive_coaching' ),
    path('in-house-courses', in_house_courses, name='in_house_courses' ),
    path('individual-training-program-itp', individual_training_program_itp, name='individual_training_program_itp' ),
    path('intelligent-leader-program-ilp5', intelligent_leader_program_ilp5, name='intelligent_leader_program_ilp5' ),
    path('iso-robot', iso_robot, name = 'iso_robot' ),
    path('outsourcing-solutions', outsourcing_solutions, name='outsourcing_solutions' ),
    path('talent-tool', talent_tool, name='talent_tool' ),
    path('testing-examination-center', testing_examination_center, name='testing_examination_center' ),

    #About Us
	path('aboutus', aboutus, name='aboutus' ),
	path('accreditations', accreditations ,name='accreditations'),
	path('clients', clients, name='clients' ),
	path('contactus', conatctus, name='contactus' ),
	path('instructors', instructors, name='instructors' ),
]