from django.shortcuts import render
from django.http import HttpResponse

from .models import SecurityGroup


def index(request):
    groups = SecurityGroup.objects.all()
    output = ', '.join([g.custom_field for g in groups])
    return HttpResponse(output)
