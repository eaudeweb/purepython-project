from django.conf.urls import patterns, include, url
from django.contrib import admin

from fb.views import index, post_details

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^post/(?P<pk>\d)/$', post_details, name='post_details'),
    url(r'^admin/', include(admin.site.urls)),
)
