from django.db import models

# Create your models here.

class Student(models.Model):
    email = models.EmailField() # veriable 
    name = models.CharField(max_length=50) # veriable 

    def __str__(self): #Construcuter
        return self.name
    
    
    
class Img(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='test_imgs/')    
    
    def __str__(self):
        return self.name
    
    
class Registration(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    add = models.TextField(default='')
    password = models.CharField(max_length=8)
        
    def __str__(self):
        return self.name
    
    
class category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cat_img')
    discription = models.TextField()
    
    def __str__(self):
        return self.name