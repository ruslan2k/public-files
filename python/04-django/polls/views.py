from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

import pprint as pp

from .forms import GroupForm
from django.contrib.auth.models import Group

def index(request):
    all_groups = Group.objects.all()
    groups = [{'id':g.id, 'name':g.name} for g in all_groups]
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GroupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pp.pprint(form.cleaned_data)
            group = Group(name=form.cleaned_data['group_name'])
            group.save()
            return HttpResponseRedirect('/')
    else:
        form = GroupForm()
    context = {'groups': groups, 'form': form}
    return render(request, 'polls/index.html', context)

def register(request):
    pp.pprint(request)
    form = """<form method="post">
    <input type="text" name="login">
    <input type="submit" value="login">
    </form>
    """
    return HttpResponse(form)
