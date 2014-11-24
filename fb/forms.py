from django.forms import Form, CharField, Textarea


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 5, 'cols': 40, 'placeholder': "What's on your mind?"}))


class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 4, 'cols': 50, 'placeholder': "Write a comment..."}))
