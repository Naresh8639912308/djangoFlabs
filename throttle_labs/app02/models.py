from django.db import models
# Create your models here.
from throttle_labs.app01.models import Student

class UsersMan(models.Model):
    s_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    activity_periods = models.ForeignKey(Student, related_name='activity_periods', on_delete =models.CASCADE)

    class Meta:
        db_table="app02"
        managed = True








