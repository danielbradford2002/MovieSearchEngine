from django.db import models

# Create your models here.

class User(models.Model):
    
    userID =  models.TextField(blank=True, null=True, default='0')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    dummy = models.CharField(max_length=200)
    def __str__(self):
        return self.title


