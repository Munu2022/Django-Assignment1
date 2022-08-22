from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    roll_number = models.IntegerField()
    department = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    semester_num = models.IntegerField()


class Departmant(models.Model):
    department = models.CharField(max_length=255)
    num_course = models.IntegerField()
    num_teachers = models.IntegerField()

