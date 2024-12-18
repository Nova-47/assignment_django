from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def like_count(self):
        return self.likes.count()  # 연결된 Like 개수를 반환


class Like(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.tweet.content[:20]}"
