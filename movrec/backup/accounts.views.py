from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from models import Ratings
from movrec.movies.models import Movies
import graphlab as gl
import json

# Create your views here.

def login_user(request):
  username = request.GET['username']
  password = request.GET['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirect to a success page.
    return HttpResponse('Success')
  else:
    # Return an 'invalid login' error message.
    return HttpResponse('Fail')
    
def logout_user(request):
  logout(request)
  return redirect('../index')
  
def register(request):
  return render(request, 'register.html')
  
def create_user(request):
  username = request.GET['username']
  password = request.GET['password']
  if username and password:
    is_existed = User.objects.filter(username=username).exists()
    if not is_existed:
      user = User.objects.create_user(username=username, email=username, password=password)
      return HttpResponse('Success')
    else:
      return HttpResponse('Fail')
      
def import_dummy_users(request):
    for i in range(2,943):
        username = "dummyUser" + str(i)
        password = "dummy"
        user = User.objects.create_user(id=i,username=username, email=username, password=password)
    return HttpResponse("Done")
    
def import_ratings(request):
    f = open('/home/chao-fu/mov-rec/movrec/data/ratings.csv',"r")
    next(f)
    for lines in f:
        line = lines.strip().split(",")
        rating = Ratings(userId = int(line[0]), movieId = int(line[1]), rating = int(line[2]))
        rating.save()
    return HttpResponse("Done")
      
def get_rated_movies(request):
    userId = request.GET['userId']
    rated_list = Ratings.objects.filter(userId = userId)
    ret = []
    for movie in rated_list:
        movieId = getattr(movie, 'movieId')
        title = Movies.objects.get(id = movieId)
        item = {}
        item['title'] = str(title)
        item['rating'] = str(getattr(movie,'rating'))
        ret.append(item)
    result = json.dumps(ret)
    return HttpResponse(result,content_type="application/json")
    
def get_recommended_movies(request):
    userId = request.GET['userId']
    model = gl.load_model("movie_model")
    #recommendations after first 50 are considered useless
    results = model.recommend(gl.SArray(data=[userId]),exclude_known=True,k=50)
    ret = []
    ret_num = 0
    for movie in results:
        item = {}
        movieId = movie['movieId']
        title = Movies.objects.get(id = movieId)
        is_existed = Ratings.objects.filter(userId=userId,movieId=movieId).exists()
        if(not is_existed):
            item['movieId'] = movieId
            item['title'] = str(title)
            ret.append(item)
            ret_num = ret_num + 1
        if(ret_num>=10):
            break
    result = json.dumps(ret)  
    return HttpResponse(result,content_type="application/json")
    
def rate_movie(request):
    movieId = request.GET['movieId']
    rating = request.GET['rating']
    userId = request.GET['userId']
    is_existed = Ratings.objects.filter(userId=userId,movieId=movieId).exists()
    if is_existed:
        return HttpResponse("Duplicated")
    else:
        rating_record = Ratings(userId = userId, movieId = movieId, rating = rating)
        rating_record.save()
        #update movie table (movieId,num_stars,num_users)
        movie = Movies.objects.get(id=movieId)
        movie.num_stars = movie.num_stars + int(rating)
        movie.num_users = movie.num_users + 1
        movie.avg_rating = float(movie.num_stars)/float(movie.num_users)
        movie.save()
        return HttpResponse("Added")
