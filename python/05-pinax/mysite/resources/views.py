from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from resources.models import Resource

import pprint as pp

from .forms import ResourceForm
#from django.contrib.auth.models import Group

def index(request):
    resources = Resource.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pp.pprint(form.cleaned_data)
            resource = Resource( \
                    name=form.cleaned_data["resource_name"],
                    user_id=0
            )
            resource.save()
            return HttpResponseRedirect('/resources')
    else:
        form = ResourceForm()
    context = {"resources": resources, "form": form}
    return render(request, "resources/index.html", context)

