from django.shortcuts import render
from django.http import HttpResponse 
# from django.Views import Views
# Create your views here.




def index(request):
    return HttpResponse("Hello, world. You're at the student Application.")