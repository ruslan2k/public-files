from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required

from resources.models import Resource, Item

import pprint as pp

from .forms import ResourceForm, ItemForm
#from django.contrib.auth.models import Group

@login_required(login_url='/accounts/login/')
def index(request):
    pp.pprint(request.user)
    resources = request.user.resource_set.all()
    #resources = Resource.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pp.pprint(form.cleaned_data)
            resource = Resource(name=form.cleaned_data["resource_name"], user_id=request.user.id)
            resource.save()
            return HttpResponseRedirect('/resources')
    else:
        form = ResourceForm()
    context = {"resources": resources, "form": form}
    return render(request, "resources/index.html", context)


@login_required(login_url='/accounts/login/')
def detail(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Item(key=form.cleaned_data["item_key"], val=form.cleaned_data["item_val"],
                    resource_id=resource_id)
            item.save()
            return HttpResponseRedirect("/resources/%s/" % resource_id)
    else:
        form = ItemForm()
    context = {"resource": resource, "form": form}
    return render(request, "resources/detail.html", context)


def delete_item(request, item_id):
    pass
