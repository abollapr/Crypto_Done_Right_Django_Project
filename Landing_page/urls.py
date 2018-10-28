from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/$', views.register),
    url(r'^profile/$', views.landing_page),
    url(r'^preview/$', views.preview_landing_page)
]
