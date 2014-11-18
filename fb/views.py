from django.shortcuts import render, redirect

from fb.models import UserPost
from fb.forms import UserPostForm


def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            post = UserPost(text=text)
            post.save()
        return redirect('index')
