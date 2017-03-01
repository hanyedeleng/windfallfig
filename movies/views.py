from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie
from movies.forms import NavSearchForm
from django.db.models import Q
# Create your views here.

# main page
def index(request):
    currentMovie_list = Movie.objects.latest('pubdate')
    context_dict = {'movie': currentMovie_list}
    return render(request,'movies/index.html',context_dict)

# about page
def about(request):
    return render(request,'movies/about.html')

# history page
def history(request):
    currentMovie_list = Movie.objects.order_by('pubdate')
    context_dict = {'movies': currentMovie_list}
    return render(request,'movies/history.html',context_dict)

# search page
def search(request):
    if request.method == 'GET':
        form = NavSearchForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data['keywords'])
            keyword = form.cleaned_data['keywords']
            qset = Q()
            for term in keyword.split():
                qset |= Q(name__contains=term)
            result_list = Movie.objects.filter(qset)
            contect_dict = {'movies': result_list}
            return render(request, 'movies/search_result.html', contect_dict)
    #if request.GET.has_key('keywords'):
    #    result_list = Movie.objects.filter(keyword)
    #     contect_dict = {'movies': result_list}
    #     return render(request, 'movies/search_result.html', contect_dic)
    return render(request, 'movies/no_result.html')
