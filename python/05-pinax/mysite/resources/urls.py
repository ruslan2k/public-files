from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<resource_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<resource_id>[0-9]+)/item/(?P<item_id>[0-9]+)/delete/$', views.delete_item, name='delete_item'),
]
