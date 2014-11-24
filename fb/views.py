from django.shortcuts import render

from fb.models import UserPost, UserPostComment
from fb.forms import UserPostForm, UserPostCommentForm


def index(request):
    posts = UserPost.objects.all()
    if request.method == 'GET':
        form = UserPostForm()
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            post = UserPost(text=text)
            post.save()

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'index.html', context)


def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)

    if request.method == 'GET':
        form = UserPostCommentForm()
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            comment = UserPostComment(text=cleaned_data['text'], post=post)
            comment.save()

    comments = UserPostComment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'post_details.html', context)
