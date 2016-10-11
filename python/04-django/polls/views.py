from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

import pprint as pp


def index(request):
    all_groups = Group.objects.all()
    output = ', '.join([g.name for g in all_groups])
    return HttpResponse(output)

def register(request):
    pp.pprint(request)
    form = """<form method="post">
    <input type="text" name="login">
    <input type="submit" value="login">
    </form>
    """
    return HttpResponse(form)
