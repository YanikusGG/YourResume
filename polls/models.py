from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_name = models.CharField(max_length=50)
    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()

    about_education = models.TextField()
    about_work_expirience = models.TextField()
    about_me = models.TextField()
