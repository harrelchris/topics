from django.template.response import TemplateResponse

from content.models import Category, Topic, Discussion


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
    return TemplateResponse(
        request=request,
        template="content/discussion_detail.html",
        context={
            "discussion": Discussion.objects.get(pk=pk),
        },
    )
