from django.conf.urls import url
from . import views
urlpatterns = [
                url(r'^liked/(?P<article_id>\d+)', views.like),
                url(r'^thisone/(?P<article_id>\d+)/$', views.thisone),
                url(r'^add',views.add),
                url(r'^$', views.articles),
                url(r'^(?P<art_category>.+)/$', views.articles),
               ]