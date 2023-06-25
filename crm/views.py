from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Courses,Enroll,Demo,DemoAttend,Student
from .forms import LoginForm,DemoForm,CreateStaffForm,StudentForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

def home(request):
    return render(request,'crm/home.html')

def course(request):
    data=Courses.objects.all()
    return render(request,'crm/course.html',{'data':data})

def course_details(request,cname):
    data=Courses.objects.filter(cname=cname)
    return render(request,'crm/coursedetail.html',{'data':data})

def enroll(request):
    if request.method=='POST':
        sname=request.POST['name']
        semail=request.POST['email']
        phone=request.POST['phonenumber']
        course=request.POST['course']
        obj=Enroll(name=sname,email=semail,phone_number=phone,course=course)
        obj.save()
        messages.success(request,'your request has been sent successfully our team will be contact you soon')
        return redirect('home')
    return render(request,'crm/enroll.html')

def coursessearch(request):
    if request.method == 'POST':
        t=request.POST['word']
        courses=Courses.objects.filter(cname__icontains=t)
        context={'data':courses}
        return render(request,'crm/coursesearch.html',context)
    return render(request,'crm/coursesearch.html')

@login_required(login_url='loginurl')
def adminhome(request):
    return render(request,'admin/adminhome.html')

@login_required(login_url='loginurl')
def enrolledlist(request):
    data=Enroll.objects.all()
    return render(request,'admin/enrolledlist.html',{'data':data})

@login_required(login_url='loginurl')
def coursesearch(request):
    if request.method == 'POST':
        t=request.POST['word']
        data=Enroll.objects.filter(course__icontains=t)
        return render(request,'admin/coursesearch.html',{'data':data})
    return render(request,'admin/coursesearch.html')


# def loginpage(request):
#     obj=LoginForm()
#     if request.method == 'POST':
#         dataobj=LoginForm(request.POST)
#         if dataobj.is_valid():
#             uname=dataobj.cleaned_data['username']
#             pwd=dataobj.cleaned_data['pwd']
#             valid_user=authenticate(request,username=uname,password=pwd)
#             if valid_user !=None:
#                 login(request,valid_user)
#                 return redirect('adminhomeurl')
#             else:
#                 messages.error(request,dataobj.errors)
#                 return render(request,'app2/login2.html',{'form':obj})
#     return render(request,'app2/login2.html',{'form':obj})

def loginpage(request):
    obj=LoginForm()
    if request.method == 'POST':
        dataobj=LoginForm(request.POST)
        if dataobj.is_valid():
            uname=dataobj.cleaned_data['username']
            pwd=dataobj.cleaned_data['pwd']
            validuser=authenticate(request,username=uname,password=pwd)
            if validuser !=None:
                login(request,validuser)
            
            if validuser.is_superuser:
                # Superuser view
                return redirect('adminhomeurl')
            elif validuser.is_staff:
                # Staff member view
                return redirect('adminhomeurl')
            else:
                # Regular user view
                return redirect('studenthomeurl')
        else:
            # Invalid credentials, show an error message
            return render(request, 'app2/login2.html', {'error': 'Invalid username or password','form':obj})
    else:
        return render(request,'app2/login2.html',{'form':obj})


def logoutpage(request):
    logout(request)
    return redirect('home')

@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
@login_required(login_url='loginurl')
def adddemo(request):
    print(request.user.username)
    obj=DemoForm()
    if request.method=='POST':
        dataobj=DemoForm(request.POST)
        if dataobj.is_valid():
            dataobj.save()
            data=Demo.objects.all()
            context={'form':obj,'data':data}
            messages.success(request,'data added successfully')
            return render(request,'admin/adddemo.html',context)
        else:
            data=Demo.objects.all()
            return render(request,'admin/adddemo.html',{'form':dataobj,'data':data})
    data=Demo.objects.all()
    return render(request,'admin/adddemo.html',{'form':obj,'data':data})


def demo_show(request):
    data=Demo.objects.all()
    return render(request,'crm/demoshow.html',{'data':data}) 

@login_required(login_url='loginurl')
def moverecords(request, record_id):
    specific_record = Enroll.objects.get(id=record_id)
    destination_record = DemoAttend.objects.create(StudentName=specific_record.name,Email=specific_record.email,Mobile=specific_record.phone_number,course=specific_record.course)
    specific_record.delete()
    return redirect('enrolledlisturl')

@login_required(login_url='loginurl')
def demoattended_students(request):
    data=DemoAttend.objects.all()
    return render(request,'admin/demoattend.html',{'data':data})

@login_required(login_url='loginurl')
def demosearch(request):
    if request.method == 'POST':
        t=request.POST['word']
        data=DemoAttend.objects.filter(course__icontains=t)
        return render(request,'admin/demoattend.html',{'data':data})
    return render(request,'admin/demoattend.html')



def register(request):
    obj=CreateStaffForm
    if request.method=='POST':
        dataobj=CreateStaffForm(request.POST)
        if dataobj.is_valid():
            dataobj.save()
            return redirect('loginurl')
        else:
            messages.error(request,dataobj.errors)
            return render(request,'admin/register.html',{'form':obj})
    return render(request,'admin/register.html',{'form':obj})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginurl')
    else:
        form = StudentForm()
    
    context = {'form': form}
    return render(request, 'admin/add_student.html', context)

@login_required
def student_home(request):
    student = request.user.student  # Assuming you have a OneToOneField relationship with the Student model
    return render(request, 'app2/studenthome.html', {'student': student})


