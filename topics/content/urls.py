from django.urls import path

from . import views

app_name = "content"

urlpatterns = [
    path("", views.topic_list, name="topic_list"),
    path("t/<int:pk>/", views.topic_detail, name="topic_detail"),
    path("d/<int:pk>/", views.discussion_detail, name="discussion_detail"),
]
