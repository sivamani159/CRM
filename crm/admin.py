from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display=['cname','image','description','keyfeatures']

@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_number','course']

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display=['did','coursename','faculty','event_time','event_date','demotype']

@admin.register(DemoAttend)
class DemoAttendAdmin(admin.ModelAdmin):
    list_display=['StudentName','Email','Mobile','course']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['user']
