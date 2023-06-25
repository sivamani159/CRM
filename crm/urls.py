from django.urls import path
from crm import views


urlpatterns=[
    path('course',views.course,name='courseurl'),
    path('coursedetail/<str:cname> ',views.course_details,name='coursedetailsurl'),
    path('enroll',views.enroll,name='enrollurl'),
    path('coursesearch',views.coursessearch,name='coursessearchurl'),
    path('adminhome',views.adminhome,name='adminhomeurl'),
    path('enrolledlist',views.enrolledlist,name='enrolledlisturl'),
    path('loginpage',views.loginpage,name='loginurl'),
    path('logout',views.logoutpage,name='logouturl'),
    path('coursesearch/',views.coursesearch,name='coursesearchurl'),
    path('adddemo',views.adddemo,name='adddemourl'),
    path('demoshow',views.demo_show,name='demoshowurl'),
    path('demoattend/<int:record_id>',views.moverecords,name='demoattendurl'),
    path('demoattended_students',views.demoattended_students,name='demoattendstudentsurl'),
    path('demosearch/coursewise',views.demosearch,name='demosearchurl'),
    path('register',views.register,name='registerurl'),
    path('addstudent',views.add_student,name='addstudenturl'),
    path('studenthome',views.student_home,name='studenthomeurl'),
]