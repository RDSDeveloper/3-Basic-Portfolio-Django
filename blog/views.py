from django.shortcuts import render

def render_posts(request):
    return render(request, "post.html")