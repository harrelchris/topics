from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.template.response import TemplateResponse

from content.models import Category, Topic, Discussion, Comment


def topic_list(request):
    return TemplateResponse(
        request=request,
        template="content/topic_list.html",
        context={
            "categories": Category.objects.all(),
        },
    )


def topic_detail(request, pk):
    return TemplateResponse(
        request=request,
        template="content/topic_detail.html",
        context={
            "topic": Topic.objects.get(pk=pk),
        },
    )


def discussion_detail(request, pk):
    comments = Comment.objects.filter(discussion_id=pk)
    paginator = Paginator(comments, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return TemplateResponse(
        request=request,
        template="content/discussion_detail.html",
        context={
            "discussion": Discussion.objects.get(pk=pk),
            "page_obj": page_obj,
        },
    )


def user_detail(request, pk):
    return TemplateResponse(
        request=request,
        template="content/user_detail.html",
        context={
            "user": User.objects.get(pk=pk),
            "discussions": Discussion.objects.filter(author_id=pk)[:5],
            "comments": Comment.objects.filter(author_id=pk)[:5],
        },
    )


def user_comments(request, pk):
    comments = Comment.objects.filter(author_id=pk)
    paginator = Paginator(comments, 50)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return TemplateResponse(
        request=request,
        template="content/user_comments.html",
        context={
            "user": User.objects.get(pk=pk),
            "page_obj": page_obj,
        },
    )


def user_discussions(request, pk):
    discussions = Discussion.objects.filter(author_id=pk)
    paginator = Paginator(discussions, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return TemplateResponse(
        request=request,
        template="content/user_discussions.html",
        context={
            "user": User.objects.get(pk=pk),
            "page_obj": page_obj,
        },
    )
