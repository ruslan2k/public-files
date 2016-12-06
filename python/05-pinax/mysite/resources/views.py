from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required

from resources.models import Resource, Item

import pprint as pp
import account.views

from .forms import ResourceForm, ItemForm, DelItemForm
#from django.contrib.auth.models import Group


class SignupView(account.views.SignupView):

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        pp.pprint(self.created_user.__dict__)
        #pp.pprint(self.created_user.smart_user)
        #pp.pprint(self.created_user.smartuser)
        #smartuser = self.created_user.smartuser
        #smartuser.salt = "bla-bla-bla"
        #smartuser.save()


class LoginView(account.views.LoginView):

    def after_login(self, form):
        pp.pprint("after_login")
        #pp.pprint(form.cleaned_data["password"])
        self.update_session(form)
        super(LoginView, self).after_login(form)

    def update_session(self, form):
        smart_user = self.login_user
        pp.pprint(smart_user)


@login_required(login_url='/accounts/login/')
def index(request):
    if not request.session.has_key('test'):
        request.session['test'] = 10
    else:
        request.session['test'] = request.session['test'] + 1
    pp.pprint(request.session['test'])
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
    resources = request.user.resource_set.all()
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


@login_required(login_url='/accounts/login/')
def delete_item(request, resource_id, item_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    item = get_object_or_404(Item, pk=item_id)
    if resource.user_id != request.user.id or resource.id != item.resource_id:
        raise Http404
    if request.method == 'POST':
        form = DelItemForm(request.POST)
        if form.is_valid():
            item.delete()
            return HttpResponseRedirect("/resources/%s/" % resource_id)
    else:
        form = DelItemForm()
    context = {"form": form}
    return render(request, "items/delete.html", context)


