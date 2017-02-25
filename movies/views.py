from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
# Create your views here.

# main page
def index(request):
    currentMovie_list = Movie.objects.latest('name')
    context_dict = {'movie': currentMovie_list}
    return render(request,'movies/index.html',context_dict)

# about page
def about(request):
    return render(request,'movies/about.html')
