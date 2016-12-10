import django
import os

os.environ["DJANGO_SETTINGS_MODULE"]="mysite.settings"
django.setup()

from django.contrib.auth.models import User
from test2.models import Profile

print(Profile.objects.all())

u1 = User(username='u1', email='u1@examle.com')
u1.save()


p = Profile(random_salt='123', user=u1)
p.save()
