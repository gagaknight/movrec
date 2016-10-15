from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
from models import Movies
import json

# Create your views here.
    
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
