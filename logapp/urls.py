from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout)
]