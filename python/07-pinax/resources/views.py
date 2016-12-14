import account.views
import base64
import hashlib
import pprint as pp
import os


#from django.shortcuts import render


def getSymKey_b64(password, salt):
    bin_salt = base64.b64decode(salt)
    bin_pass = hashlib.sha256(password.encode('utf-8')).digest()
    bk = hashlib.pbkdf2_hmac('sha256', bin_pass, bin_salt, 100000)
    return base64.b64encode(bk).decode('ascii')


class SignupView(account.views.SignupView):

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

    def update_profile(self, form):
        password = form.cleaned_data['password']
        salt = self.created_user.profile.salt
        sym_key = getSymKey_b64(password, salt)
        if 'sym_key' in self.request.session:
            print('secret exists')
        else:
            print('secret NOT exists')
            self.request.session['sym_key'] = sym_key
        print(self.request.session['sym_key'])

