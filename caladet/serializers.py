from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Tweet


class TweetSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ('tweet_text', 'tweet_language', 'pub_date')