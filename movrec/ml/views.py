from django.shortcuts import render
from django.http import HttpResponse
from movrec.accounts.models import Ratings
import graphlab as gl

def dump_ratings_csv(request):
    ratings = Ratings.objects.all()
    f = open("data/ratings.csv","w")
    f.write("userId, movieId, rating\n")
    for item in ratings:
        movieId = getattr(item, 'movieId')
        userId = getattr(item, 'userId')
        rating = getattr(item,'rating')
        f.write(str(userId) + "," + str(movieId) + "," + str(rating)+"\n")
    f.close()
    return HttpResponse("Done")
    
def retrain_model(request):
    dump_ratings_csv(request)
    items = gl.SFrame.read_csv('/home/chao-fu/mov-rec/movrec/data/movies.csv')
    actions = gl.SFrame.read_csv('/home/chao-fu/mov-rec/movrec/data/ratings.csv')
    actions = actions[actions['rating'] >=4 ]
    model = gl.recommender.create(actions, 'userId', 'movieId',target="rating")
    model.save("movie_model")
    return HttpResponse("Done")
# Create your views here.
