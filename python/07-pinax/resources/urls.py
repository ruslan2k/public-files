from django.conf.urls import url

from . import views

urlpatterns = [
    # /resources/
    url(r'^$', views.index, name='index'),
    # /resources/5/
    url(r'^(?P<resource_id>[0-9]+)/$', views.detail, name='detail'),
    # /resources/test/
    url(r'^test/$', views.test, name='test'),
]

