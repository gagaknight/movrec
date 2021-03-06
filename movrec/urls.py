"""movrec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from accounts.views import login_user
from accounts.views import logout_user
from accounts.views import register
from accounts.views import create_user
from accounts.views import get_rated_movies
from accounts.views import get_recommended_movies
from accounts.views import rate_movie
from index.views import mov_rec
from movies.views import get_highest_avg_rating
from ml.views import dump_ratings_csv
from ml.views import retrain_model

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login_user/$',login_user),
    url(r'^index/$',mov_rec),
    url(r'^logout/$',logout_user),
    url(r'^register/$',register),
    url(r'^create_user/$',create_user),
    url(r'^get_highest_avg_rating/$',get_highest_avg_rating),
    url(r'^get_rated_movies/$',get_rated_movies),
    url(r'^get_recommended_movies/$',get_recommended_movies),
    url(r'^rate_movie/$',rate_movie),
    url(r'^dump_ratings_csv/$',dump_ratings_csv),
    url(r'^retrain_model/$',retrain_model),
]
