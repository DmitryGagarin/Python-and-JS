from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    time_created = models.DateTimeField(auto_now_add=True)
    
    