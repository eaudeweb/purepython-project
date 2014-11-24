from django.db import models


class UserPost(models.Model):
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default='Eau De Web', max_length=20)

    def __unicode__(self):
        return '{} @ {}'.format(self.author, self.date_added)

    class Meta:
        ordering = ['-date_added']


class UserPostComment(models.Model):
    text = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default='Eau De Web', max_length=20)

    post = models.ForeignKey(UserPost)

    def __unicode__(self):
        return '{} @ {}'.format(self.author, self.date_added)

    class Meta:
        ordering = ['date_added']
