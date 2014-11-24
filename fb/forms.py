from django.forms import Form, CharField, Textarea, PasswordInput


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 5, 'cols': 40, 'placeholder': "What's on your mind?"}))


class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 4, 'cols': 50, 'placeholder': "Write a comment..."}))


class UserLogin(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)
