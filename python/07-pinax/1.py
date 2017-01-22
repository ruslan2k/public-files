import django
import os
import random

os.environ["DJANGO_SETTINGS_MODULE"]="mysite.settings"
django.setup()

from django.contrib.auth.models import User
from resources.models import Profile

#print(Profile.objects.all())

user_name = 'user{}'.format(random.randrange(10, 99))

u = User(username=user_name, email='{}@examle.com'.format(user_name))
u.save()


#p = Profile(random_salt='123', user=u)
#p.save()
