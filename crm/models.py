from django.db import models
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.hashers import make_password

# Create your models here.
class Courses(models.Model):
    cname=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/')
    description=models.TextField(null=True)
    keyfeatures=models.TextField(null=True)

class Enroll(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_number = models.CharField(max_length=10)
    course=models.CharField(max_length=40)

class Demo(models.Model):
    did=models.IntegerField(primary_key=True)
    COURSE_CHOICES = [
        ('PYTHON', 'Python'),
        ('DEVOPS', 'DevOps'),
        ('TESTING', 'Testing'),
        ('JAVA', 'Java'),
        ('POWERBI', 'PowerBI'),
    ]
    coursename=models.CharField(max_length=100, choices=COURSE_CHOICES)
    faculty=models.CharField(max_length=20)
    event_date=models.DateField(null=True)
    event_time=models.TimeField(null=True)
    DEMO_CHOICES = [
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
        ('ONLINE_OFFLINE', 'Online/Offline'),
    ]
    demotype=models.CharField(max_length=30,choices=DEMO_CHOICES)

class DemoAttend(models.Model):
    
    StudentName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=40)
    Mobile = models.CharField(max_length=10)
    course = models.CharField(max_length=20,null=True)
     
    def __str__(self):
        return self.StudentName
    

@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Registered successfully'
        password = instance.password
        message = f'Hi {instance.username},\n\n' \
                  f'Thank you for registering. Below are your login credentials:\n\n' \
                  f'Username: {instance.username}\n' \
                  f'Password: {password}\n\n' \
                  f'Please keep your credentials confidential.\n\n' \
                  f'Best regards,\nTeam VCUBE'
        from_user = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_user, [instance.email])

post_save.connect(send_registration_email, sender=User)






class Student(models.Model):
    COURSE_CHOICES = (
        ('Python', 'Python'),
        ('Python Full Stack', 'Python Full Stack'),
        ('DevOps', 'DevOps'),
        ('AWS', 'AWS'),
        ('MySQL', 'MySQL'),
        ('Java', 'Java'),
        ('Java Full Stack', 'Java Full Stack'),
        ('Testing', 'Testing'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joining_date = models.DateField()
    actual_fees = models.DecimalField(max_digits=8, decimal_places=2)
    fees_paid = models.DecimalField(max_digits=8, decimal_places=2)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.course}"













