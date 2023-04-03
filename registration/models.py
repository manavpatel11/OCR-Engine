from django.db import models

class users_data(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    wallet = models.CharField(max_length=100)
    
    