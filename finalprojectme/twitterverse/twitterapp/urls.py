from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("results",views.results, name="results"),
    path("eventmenu",views.eventmenu, name="events"),
    path("trending",views.trending, name="trends"),
    path("addfollowing",views.addfollowing, name="addfoll"),
    path("uefa",views.showUEFA, name="showuefa"),
    path("following",views.following, name="following"),
    path('signup', views.signup, name='signup'),
    path("resultstrend<str:trend>",views.resultstrend, name="resultstrend"),
    ]
