from django.shortcuts import render
from portfolio.models import Project


def render_posts(request):
    projects=Project.objects.all()

    return render(request, "post.html", {"projects":projects})