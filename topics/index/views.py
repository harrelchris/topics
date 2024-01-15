from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(
        request=request,
        template="index/index.html",
        context={},
    )
