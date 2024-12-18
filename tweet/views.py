from django.shortcuts import render
from .models import Tweet


from django.db import models

class Tweet(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


def tweet_list(request):
    tweets = Tweet.objects.all()  # 모든 Tweet 가져오기
    return render(request, "tweets/tweet_list.html", {"tweets": tweets})
