import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','windfallfig.settings')

import django
django.setup()
from movies.models import Movie

def populate():

    all_movies = [
            {
                "name":"Hachi: A Dog's Tale",
                "pubdate":"2017-07-19T14:59:50+0000",
                "posterpath":"images/hachi.jpg",
                "basicinfo":"Director: Lasse Hallström;Writers: Stephen P. Lindsey (screenplay), Kaneto Shindô (motion picture "Hachiko monogatari");Stars: Richard Gere, Joan Allen, Cary-Hiroyuki Tagawa ",
                "synopsis":"The true story about a dog's loyalty to its master, even after his death.",
                "relatedlinks":"http://www.imdb.com/title/tt1028532/"
            },
            {
                "name":"Sully",
                "pubdate":"2017-04-05T22:26:50+0000",
                "posterpath":"images/sully.jpg",
                "basicinfo":"Director: Clint Eastwood;Writers: Todd Komarnicki, Chesley Sullenberger;Stars: Tom Hanks, Aaron Eckhart, Laura Linney",
                "synopsis":"The story of Chesley Sullenberger, an American pilot who became a hero after landing his damaged plane on the Hudson River in order to save the flight's passengers and crew.",
                "relatedlinks":"http://www.imdb.com/title/tt3263904/"
            },
            {
                "name":"Letters from Iwo Jima",
                "pubdate":"2017-03-26T22:26:50+0000",
                "posterpath":"images/Letters_from_Iwo_Jima.jpg",
                "basicinfo":"Director: Clint Eastwood;Writers: Iris Yamashita (screenplay), Iris Yamashita (story);Stars: Ken Watanabe, Kazunari Ninomiya, Tsuyoshi Ihara ",
                "synopsis":"The story of the battle of Iwo Jima between the United States and Imperial Japan during World War II, as told from the perspective of the Japanese who fought it.",
                "relatedlinks":"http://www.imdb.com/title/tt0498380/"
            },
            {
                "name":"中国合伙人",
                "pubdate":"2017-03-17T22:26:50+0000",
                "posterpath":"images/zhongguohehuoren.jpg",
                "basicinfo":"导演: 陈可辛;主演: 黄晓明 / 邓超 / 佟大为 / 杜鹃",
                "synopsis":"20世纪80年代，三个怀有热情和梦想的年轻人在高等学府燕京大学的校园内相遇，从此展开了他们长达三十年的友谊和梦想征途。",
                "relatedlinks":"https://movie.douban.com/subject/11529526/"
            },
            {
                "name":"乘风破浪",
                "pubdate":"2017-03-05T22:26:50+0000",
                "posterpath":"images/chengfeng_polang.jpg",
                "basicinfo":"导演:韩寒;主演: 邓超 / 彭于晏 / 赵丽颖",
                "synopsis":"赛车手阿浪（邓超 饰）一直对父亲（彭于晏 饰）反对自己的赛车事业耿耿于怀，在向父亲证明自己的过程中，阿浪却意外卷入了一场奇妙的冒险。他在这段经历中结识了一群兄弟好友，一同闯过许多奇幻的经历，也对自己的身世有了更多的了解",
                "relatedlinks":"https://movie.douban.com/subject/26862259/" },
            {
                "name":"Luck Key",
                "pubdate":"2017-03-01T15:32:30+0000",
                "posterpath":"images/luck_key.jpg",
                "basicinfo":"Director: Gye-byeok Lee; Writers: Kenji Uchida, Yoon-mi Jang; Stars: Hae-jin Yoo,Yun-hie Jo",
                "synopsis":"Based on the Japanese film Key of Life, this is a Korean adaptation.",
                "relatedlinks":"http://www.imdb.com/title/tt6175078/" },
            {
                "name": "The Shawshank Redemption",
                "pubdate": "2017-02-23T09:21:31+0000",
                "posterpath":"images/shawshank_redemption.jpg",
                "basicinfo":"Director:Frank Darabont;Writes:Stephen King,Frank Darabont;Stars:Tim Robbins, Morgan Freeman, Bob Gunton",
                "synopsis":"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                "relatedlinks":"http://www.imdb.com/title/tt0111161/" },
            {
                "name":"Forrest Gump",
                "pubdate":"2017-02-16T09:21:31+0000",
                "posterpath":"images/forrest_gump.jpg",
                "basicinfo":"Director: Robert Zemeckis;Writers: Winston Groom, Eric Roth;Stars: Tom Hanks, Robin Wright, Gary Sinise",
                "synopsis":"Forrest Gump, while not intelligent, has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                "relatedlinks":"http://www.imdb.com/title/tt0109830/" },
            {
                "name":"Test data 1",
                "pubdate":"2011-11-17T09:21:31+0000",
                "posterpath":"images/projector.jpg",
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
