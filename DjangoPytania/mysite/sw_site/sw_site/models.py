from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    is_recruiter = models.BooleanField()
    # recruiter = models.BooleanField(default=False)




