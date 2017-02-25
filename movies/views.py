from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# main page
def index(request):
    return render(request,'movies/index.html')

# about page
def about(request):
    return render(request,'movies/about.html')
