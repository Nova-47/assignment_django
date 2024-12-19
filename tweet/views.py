from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Tweet
from .serializers import TweetSerializer


class AllTweetsView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


class UserTweetsView(APIView):
    def get(self, request, user_id):
        tweets = Tweet.objects.filter(user_id=user_id)
        if not tweets.exists():
            raise NotFound("User not found or no tweets by the user.")
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
