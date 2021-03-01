from rest_framework import serializers
from .models import Student

class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("s_num","s_no", "start_time","end_time")

class LogTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("start_time", "end_time")