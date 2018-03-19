from django.http import HttpResponse
from django.template import loader
from django.core import serializers
import datetime
from caladet.language_detection.language.Emojis import Emojis
from caladet.language_detection import tweetparser, language_detection

from .models import Tweet

from .serializers import TweetSerializer
from rest_framework import generics

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    latest_tweets_list = Tweet.objects.order_by('-pub_date')[:5]
    template = loader.get_template('caladet/index.html')
    context = {
        'latest_tweets_list': latest_tweets_list,
    }

    if request.method == 'POST':
        clean_tweet = tweetparser.Tweet.parsetweet(request.POST['tweet_entry'], Emojis)
        if language_detection.classify(clean_tweet) == 'cat':
            result = '1'
        else:
            result = '0'
        print(result)
        tweet = Tweet.objects.create(tweet_text=request.POST['tweet_entry'], tweet_language=result,
                                     pub_date=datetime.datetime.now())
        tweet.save()
        context = {
            'latest_tweets_list': latest_tweets_list,
            'tweet_language': result,
            'tweet_text': request.POST['tweet_entry'],
        }

    return HttpResponse(template.render(context, request))


@csrf_exempt
def postAPI(request):
    if request.method == 'POST':
        print(request.POST)
        clean_tweet = tweetparser.Tweet.parsetweet(request.POST['tweet_entry'], Emojis)
        if language_detection.classify(clean_tweet) == 'cat':
            result = '1'
        else:
            result = '0'
        print(result)
        tweet = Tweet.objects.create(tweet_text=request.POST['tweet_entry'], tweet_language=result,
                                     pub_date=datetime.datetime.now())
        tweet.save()

        return HttpResponse(serializers.serialize('json', [tweet, ]), content_type='application/json')


class APITweetList(generics.ListCreateAPIView):
    model = Tweet
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
