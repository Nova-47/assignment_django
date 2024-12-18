from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),  # / 경로에 tweet_list 뷰 연결
]
