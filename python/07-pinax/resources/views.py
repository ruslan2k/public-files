import base64
import account.views
import pprint as pp
import os

#from django.shortcuts import render

# TODO
# http://blog.pinaxproject.com/2015/10/12/recap-september-pinax-hangout/
# http://django-user-accounts.readthedocs.io/en/latest/usage.html


class SignupView(account.views.SignupView):

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        print('update_profile')
        profile = self.created_user.profile
        print('DEBUG profile.salt')
        print(profile.salt)
        print('DEBUG self.request.session')
        if 'secret' in self.request.session:
            print('secret exists')
        else:
            print('secret NOT exists')
            secret = base64.b64encode(os.urandom(4)).decode('ascii')
            self.request.session['secret'] = secret
        print(self.request.session['secret'])

