from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
from models import Movies
import json

# Create your views here.

def import_movies(request):
    f = open('data/movie_table.txt',"r");
    for lines in f:
        line = lines.strip().split("\t")
        movie = Movies(title = line[0],num_stars=int(line[1]),num_users=int(line[2]),avg_rating=float(line[1])/float(line[2]))
        movie.save()
    return HttpResponse('Done')
    
def get_highest_avg_rating(reqeust):
    rec_movie = Movies.objects.order_by('-avg_rating')[:10]
    ret = []
    for movie in rec_movie:
    	item = {}
        item['title'] = str(movie) 
        item['avg_rating'] = float(getattr(movie, 'avg_rating'))
        ret.append(item)
    result = json.dumps(ret)
    return HttpResponse(result,content_type="application/json")
