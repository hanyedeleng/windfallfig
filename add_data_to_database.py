import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','windfallfig.settings')

import django
django.setup()
from movies.models import Movie

def populate():

    all_movies = [ 
            {
                "name": "The Shawshank Redemption",
                "pubdate": "2017-11-17T09:21:31+0000",
                "posterpath":"images/shawshank_redemption.jpg",
                "basicinfo":"Director:Frank Darabont;Writes:Stephen King,Frank Darabont;Stars:Tim Robbins, Morgan Freeman, Bob Gunton",
                "synopsis":"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                "relatedlinks":"http://www.imdb.com/title/tt0111161/" },
            {
                "name":"Test data 1",
                "pubdate":"2011-11-17T09:21:31+0000",
                "posterpath":"images/maybelogo.jpeg",
                "basicinfo":"this is a test data",
                "synopsis":"need to add something else",
                "relatedlinks":"http://www.google.com/" }
            ] 

    # add date to datebase
    for m in all_movies:
        print(m["name"])
        add_movie(m["name"],m["pubdate"],m["posterpath"],m["basicinfo"],m["synopsis"],m["relatedlinks"])

def add_movie(name, pubdate, posterpath, basicinfo, synopsis, relatedlinks):
    newmovie = Movie.objects.get_or_create(name=name)[0]
    # movie.name = name 
    newmovie.pubdate = pubdate
    newmovie.posterpath = posterpath
    newmovie.basicinfo = basicinfo
    newmovie.synopsis = synopsis
    newmovie.relatedlinks = relatedlinks
    newmovie.save()
    return newmovie

# Start execution here!
if __name__ == '__main__':
    print("Starting Movie population script...")
    populate()
