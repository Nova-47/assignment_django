from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # User의 username을 문자열로 표시

    class Meta:
        model = Tweet
        fields = ["id", "content", "created_at", "user"]
