from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^disqus/$', views.disqus, name='disqus'),
    url(r'^(?P<subject_name>[\w|\W]+)/1$', views.detail, name='detail'),
    url(r'^(?P<subject_name>[\w|\W]+)/(?P<menu_item>[\w|\W]+)/$', views.objectives, name='objective'),
]