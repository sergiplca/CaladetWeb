from django.db import models

# Create your models here.


class Tweet(models.Model):
    tweet_text = models.CharField(max_length=140)
    tweet_language = models.CharField(max_length=1)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tweet_text

    def get_pub_date(self):
        return self.pub_date