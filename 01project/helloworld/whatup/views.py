from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""
Where we handle request logic for our web application. 
What needs to happen or what data needs to be present at the press of a button
"""

def frontPageView(request):
    return HttpResponse('What is going on folks. Thanks for visiting')