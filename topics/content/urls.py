from django.urls import path

from . import views

app_name = "content"

urlpatterns = [
    path("", views.topic_list, name="topic_list"),
    path("t/<int:pk>/", views.topic_detail, name="topic_detail"),
    path("d/<int:pk>/", views.discussion_detail, name="discussion_detail"),
    path("u/<int:pk>/", views.user_detail, name="user_detail"),
    path("u/<int:pk>/comments/", views.user_comments, name="user_comments"),
    path("u/<int:pk>/discussions/", views.user_discussions, name="user_discussions"),
]
