from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profiles(request):
    return HttpResponse('Welcome to the PROFILE page')