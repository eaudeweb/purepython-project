from django.shortcuts import render

from fb.models import UserPost


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'index.html', context)
