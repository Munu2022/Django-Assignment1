from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Students
from .models import Departmant

# Create your views here.
# d

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def index(request):
    mymembers = Students.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
            }
    return HttpResponse(template.render(context, request))

def index_dept(request):
    mymembers = Departmant.objects.all().values()
    template = loader.get_template('index_dept.html')
    context = {
        'mymembers': mymembers,
            }
    return HttpResponse(template.render(context, request))

def add_student(request):
  template = loader.get_template('add_student.html')
  return HttpResponse(template.render({}, request))

def add_dept(request):
  template = loader.get_template('add_dept.html')
  return HttpResponse(template.render({}, request))

def addrecord_student(request):
  x = request.POST['first']
  y = request.POST['last']
  a = request.POST['dob']
  b = request.POST['roll_number']
  c = request.POST['department']
  d = request.POST['course']
  e = request.POST['semester_num']
  Details = Students(firstname=x, lastname=y, dob=a, roll_number=b, department= c, course=d, semester_num= e)
  Details.save()
  return HttpResponseRedirect(reverse('index'))

def addrecord_dept(request):
  c = request.POST['department']
  d = request.POST['num_course']
  e = request.POST['num_teachers']
  Details = Departmant(department= c, num_course=d, num_teachers= e)
  Details.save()
  return HttpResponseRedirect(reverse('index_dept'))


def delete_student(request, id):
  Details = Students.objects.get(id=id)
  Details.delete()
  return HttpResponseRedirect(reverse('index'))

def delete_dept(request, id):
  Details = Departmant.objects.get(id=id)
  Details.delete()
  return HttpResponseRedirect(reverse('index_dept'))

def update(request, id):
  mymember = Students.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def update_dept(request, id):
  mymember = Departmant.objects.get(id=id)
  template = loader.get_template('update_dept.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  dob = request.POST['dob']
  roll_number = request.POST['roll_number']
  department = request.POST['department']
  course = request.POST['course']
  semester_num = request.POST['semester_num']
  Details = Students.objects.get(id=id)
  Details.firstname= first
  Details.lastname= last
  Details.dob= dob
  Details.roll_number= roll_number
  Details.department= department
  Details.course= course
  Details.semester_num= semester_num
  Details.save()
  return HttpResponseRedirect(reverse('index'))

def updaterecord_dept(request, id):
  department = request.POST['department']
  num_course = request.POST['num_course']
  num_teachers = request.POST['num_teachers']
  Details = Departmant.objects.get(id=id)
  Details.department= department
  Details.num_course= num_course
  Details.num_teachers= num_teachers
  Details.save()
  return HttpResponseRedirect(reverse('index_dept'))