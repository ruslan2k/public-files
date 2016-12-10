import django
import os

os.environ["DJANGO_SETTINGS_MODULE"]="mysite.settings"
django.setup()

from test2.models import Profile

p = Profile(random_salt='123')
p.save()

