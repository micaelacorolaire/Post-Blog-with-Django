from django.shortcuts import render
from rest_framework import viewsets
from .serializer import serializerlogin,serializerpersonaldatauser,serializerpublications
from .models import login,personal_data_user,publications

class loginViewSet(viewsets.ModelViewSet):#ModelViewSet es una clase del modulo viewsets
    queryset=login.objects.all() #query almacena todos los registros de la tabla login,all=todos los registros almacena
    serializer_class=serializerlogin #serializa datos de la tabla login.
    basename='login'
class personaldatauserViewSet(viewsets.ModelViewSet):
    queryset=personal_data_user.objects.all()
    serializer_class=serializerpersonaldatauser
    basename='personal_data_user'
class publicationsViewSet(viewsets.ModelViewSet): 
    queryset=publications.objects.all()
    serializer_class=serializerpublications
    basename='publications'
# Create your views here.
