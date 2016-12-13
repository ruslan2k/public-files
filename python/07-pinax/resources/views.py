import account.views

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

