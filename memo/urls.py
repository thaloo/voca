from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.voca_list, name='voca_list'),
    url(r'^delete/(?P<vocabulary>reg)/$', views.voca_del, name='voca_del'),
]
