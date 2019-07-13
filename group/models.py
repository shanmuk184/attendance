from django.db import models
from django.contrib.auth.models import Permission
# Create your models here.
from core.models import TimeStampedModel
from appAuth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Group(TimeStampedModel):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(User, through=Employee)

class Employee(TimeStampedModel):
    STANDARD = 'STD'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (PRESIDENT, 'president')
    )

    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    name = models.CharField(max_length=64)
    group = models.ForeignKey(Group, related_name='employees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='employees', on_delete=models.CASCADE)
    class Meta:
        permissions = [
                       ('can_view_attendance_lists', 'can view attendance lists')
                       ]

class Image(TimeStampedModel):
    image_url = models.URLField()
    owner = models.ForeignKey(Employee, related_name='images', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='images', blank=None, on_delete=models.CASCADE)
    type = models.CharField(max_length=64)


class Task(TimeStampedModel):
    name = models.CharField(max_length=64)
    group = models.ForeignKey(Group, related_name='tasks', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='tasks', on_delete=models.CASCADE)


class Shift(TimeStampedModel):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    group = models.ForeignKey(Group, related_name='shifts', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='shifts', on_delete=models.CASCADE)


class Target(TimeStampedModel):
    name = models.CharField(max_length=64)
    group = models.ForeignKey(Group, related_name='targets', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,related_name='targets', on_delete=models.CASCADE)

class Attendance(TimeStampedModel):
    date = models.DateTimeField()
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    location_match = models.BooleanField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

