from django.shortcuts import render
import tweepy
from tweepy import *
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment import SentimentIntensityAnalyzer
from test import *
import requests
from twitter import *
import json
from django.http import HttpResponse
from django.views import View
from twitterapp.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

#-------------------------------------------------------------------------
newsentences=[]#The sentiments for the sentences
sentences=[]# Results from the API search will be stored here
sid = SentimentIntensityAnalyzer() #Used to find feelings
#-------------------------------------------------------------------------
#Twitter Dev Keys
consumer_key = 'QLcDOtaD79Vc9zb6zc5vrqpVH'
consumer_secret = 'Sl2GOvNBBegz6YNgIHIf2tQZLY8KXjzfyMVvjhgepsZ0gUaILW'
access_token = '856096822619721728-AvtfUa0VvgnOucRAFzC4pqpva6EJe6B'
access_token_secret = 'l1wbH8ACOFh7AZ8s4AI9cOnPdc2lnK7Gxsps33DFvMFis'
#-------------------------------------------------------------------------
#Setting auth for tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#-------------------------------------------------------------------------
api = tweepy.API(auth)
#Get Trends from twitter
trends = api.trends_place(1)
data = trends[0]
trends = data['trends']
names = [trend['name'] for trend in trends]
#-------------------------------------------------------------------------
def index(request):
    # return res
    return render(request, "index.html")
#-------------------------------------------------------------------------

def results(request):
    newsentences=[]
    sentences=[]
    phrase=request.POST.get("phrase",False)
    result = api.search(phrase)
    for results in result:
        sentences.append(results.text)

    for sentence in sentences:
        ss = sid.polarity_scores(sentence)

    for k in sorted(ss):
      temp='{}: {}, '.format(k, ss[k])
      newsentences.append(temp)

    context={
      "sentences":newsentences,
      "results":sentences
    }
    return render(request, "tweets.html",context)
#-------------------------------------------------------------------------
def resultstrend(request,trend):
    #Renders results on a page
    newsentences=[]
    sentences=[]
    result = api.search(trend)
    #Adding tweet to list
    for results in result:
        sentences.append(results.text.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()))

    for sentence in sentences:
        ss = sid.polarity_scores(sentence)

    # Get integral value from sentiments
    for k in sorted(ss):
      temp='{}: {}, '.format(k, ss[k])
      newsentences.append(temp)

    context={
      "sentences":newsentences,
      "results":sentences
    }
    return render(request, "tweets.html",context)
#-------------------------------------------------------------------------
def showUEFA(request):
       # Show teams from UEFA
    context = {
       "Teams" : UEFA.objects.all()
               }
    return render(request, "UEFA.html",context)
#-------------------------------------------------------------------------
def eventmenu(request):
    #Shows upcoming events

    return render(request, "eventmenu.html")
#-------------------------------------------------------------------------
def trending(request):
    # Get tweets from twitter devs
    context={
        "names":names
    }
    return render(request, "trends.html",context)
#-------------------------------------------------------------------------
def following(request):
    # Get tweets from twitter devs
    username = request.user.username
    context={
    "follow": Following.objects.filter(Username=username)
    }
    return render(request, "following.html",context)
#-------------------------------------------------------------------------
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def view(request):
        return render(request, 'home.html')
#-------------------------------------------------------------------------
def followingadd(request):
    # Get tweets from twitter devs
    phrase=request.POST.get("phrase",False)
    username = request.user.username
    follow_instance = Following.objects.create(Username=username,Phrases=phrase)
    return render(request, "add.html")