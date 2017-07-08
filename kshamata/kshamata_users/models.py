from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.


class Women(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField(auto_now=True)
    id = models.CharField(max_length=20, primary_key=True)
    contact = models.IntegerField()
    background = models.CharField(max_length=10, null=True, blank=True)
    time_of_stay = models.IntegerField(max_length=10, null=True, blank=True)
    skills = models.CharField(max_length=20, blank=True, null=True)
    trainings = models.CharField(max_length=20, blank=True, null=True)
    level_of_skill = models.IntegerField(max_length=5, blank=True, null=True)
    cur_salary = models.IntegerField()
    cur_location = models.CharField(max_length=30, blank=True, null=True)
    future_plans = models.TextField(max_length=30, null=True, blank=True)
    remarks = models.TextField(max_length=30, null=True, blank=True)
    date_of_survey = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
