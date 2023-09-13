from django.db import models
from django.core.validators import MinValueValidator


class login(models.Model):
    email=models.CharField(max_length=15,null=False)
    password=models.CharField(max_length=20,null=False)
    active=models.BooleanField(default=True)
    
class personal_data_user(models.Model):
    name=models.CharField(max_length=20,null=False)
    lastname=models.CharField(max_length=20,null=False)
    age=models.IntegerField(validators=[MinValueValidator(18)],null=False)
    nickname=models.CharField(max_length=10,null=False)
    nacionality=models.CharField(max_length=20,null=False)
    email=models.CharField(max_length=15,null=False)
    password=models.CharField(max_length=20,null=False)
   
class publications(models.Model):
    title=models.CharField(max_length=5 , null=False)
    content=models.CharField(validators=[MinValueValidator(500)],max_length=1000,null=False)
    pub_date=models.DateTimeField(auto_now=True,null=False)
    author=models.CharField(max_length=20,null=False)
    
    
    

# Create your models here.
