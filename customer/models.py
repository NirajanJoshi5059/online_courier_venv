from tkinter import CASCADE
from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_list=models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.gender_list
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Customer(models.Model):
    first_name=models.CharField(max_length=255)
    middle_name=models.CharField(max_length=255, blank=True, null=True)
    last_name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.address}'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
