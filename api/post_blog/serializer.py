from rest_framework import serializers
from .models import login,publications,personal_data_user

class serializerlogin(serializers.ModelSerializer):
    class Meta:
        model=login
        fields=['email','password','active']

class serializerpublications(serializers.ModelSerializer):
    class Meta:
        model=publications
        fields=['title','content','pub_date','author']

class serializerpersonaldatauser(serializers.ModelSerializer):
    class Meta:
        model=personal_data_user
        fields=['name','lastname','age','nacionality','email','password','nickname']
        