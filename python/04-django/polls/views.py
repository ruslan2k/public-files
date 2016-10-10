from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group

#from .models import SecurityGroup


def index(request):
    all_groups = Group.objects.all()
    output = ', '.join([g.name for g in all_groups])
    return HttpResponse(output)
