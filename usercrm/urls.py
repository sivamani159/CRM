from django.urls import path
from usercrm import views


urlpatterns=[
    path('',views.userregister,name='userregisterurl'),

]