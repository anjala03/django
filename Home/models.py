from django.db import models

# Create your models here.
class Author (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    sex=models.CharField(max_length=10)
    email= models.EmailField(default=None)
    #this method __str__ must be defined inside that class whose object you want to represent in from of strings
    def __str__(self)-> str:
        # if just want to return one single attribute in string formate use return self.attributename, eg: self.name/self.age/self.email and so on 
        return f" {self.name}, {self.sex},{self.email}, {self.age} "
#
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    dob=models.DateField()
    adress= models.TextField()




