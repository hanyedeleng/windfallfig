from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^$',views.index,name='index'), 
    url(r'^about/',views.about,name='about'),
    url(r'^history/',views.history,name='history'),
    url(r'^search/',views.search,name='search'),
]
