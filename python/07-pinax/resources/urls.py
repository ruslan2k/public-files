from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /resources/test/
    url(r'^test/$', views.test, name='test'),
]

