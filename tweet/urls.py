from django.urls import path
from .views import AllTweetsView, UserTweetsView

urlpatterns = [
    path("api/v1/tweets", AllTweetsView.as_view(), name="all_tweets"),
    path(
        "api/v1/users/<int:user_id>/tweets",
        UserTweetsView.as_view(),
        name="user_tweets",
    ),
]
