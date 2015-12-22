from django.conf.urls import url
from . import views
urlpatterns = [
                url(r'^thisone/(?P<article_id>\d+)/$', views.thisone),
                url(r'^$',views.articles),
                url(r'^liked/(?P<article_id>\d+)', views.like)
               ]