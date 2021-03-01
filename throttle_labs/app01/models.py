from django.db import models
from throttle_labs.app02.models import UsersMan

from django.template.defaultfilters import date
from datetime import datetime

# Create your models here.

class Student(models.Model):
    s_num = models.AutoField(primary_key=True)
    s_no = models.ForeignKey(UsersMan, related_name="activity_periods", on_delete=models.CASCADE)
    start_time = models.CharField(max_length = 100)
    end_time = models.CharField(max_length=100)

    class Meta:
        db_table = "app01"
        managed = True
