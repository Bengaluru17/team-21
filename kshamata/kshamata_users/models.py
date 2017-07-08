from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Women(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False,)
    dob = models.DateField(null=False, blank=False, default=timezone.now())
    aadhar_id = models.CharField(max_length=20, primary_key=True, null=False, blank=False)
    contact = models.IntegerField(null=False, blank=False)
    background = models.CharField(max_length=20, null=True, blank=True)
    time_of_stay = models.IntegerField(null=True, blank=True)
    skills = models.CharField(max_length=20, blank=True, null=True)
    trainings = models.CharField(max_length=20, blank=True, null=True)
    level_of_skill = models.IntegerField(blank=True, null=True)
    cur_salary = models.IntegerField(blank=True, null=True)
    cur_location = models.CharField(max_length=30)
    future_plans = models.TextField(max_length=30, null=True, blank=True)
    remarks = models.TextField(max_length=30, null=True, blank=True)
    date_of_survey = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    women = models.ManyToManyField(Women)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    purpose = models.CharField(max_length=30, blank=True, null=True)
    target = models.ManyToManyField(Women)
    women_count = models.IntegerField()
    response_shelter = models.TextField(max_length=30, null=True, blank=True)
    respone_women = models.TextField(max_length=30, null=True, blank=True)