from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
#from django.contrib.auth.models import Group
from itertools import chain

import pprint as pp


#def dump_args(fn):
#    "This decorator dumps out the arguments passed to a function before calling it"
#    from itertools import chain
#    def wrapped(*v, **k):
#        name = fn.__name__
#        print("%s(%s)" % (name, ",".join(map(repr, chain(v, k.values())))))
#        return fn(*v, **k)
#    return wrapped

class Resource(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    key = models.CharField(max_length=100)
    val = models.CharField(max_length=255)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.key


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salt = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def model_post_save(*args, **kwargs):
    print('post_save')
    print("post_save(args:{})".format(",".join(map(repr, args))))
    print("post_save(kwargs.keys:{})".format(",".join(map(repr, kwargs.keys()))))
    print("post_save(kwargs.values:{})".format(",".join(map(repr, kwargs.values()))))
    #print('Saved: {}'.format(kwargs['instance'].__dict__))
    #pass


@receiver(post_save, sender=User)
def profile_post_save(instance, created, **kwargs):
    pp.pprint(instance.__dict__)
    Profile.objects.create(user=instance, salt='SALT')
    #profile.salt = 'salt-salt-salt'
    #profile.save()
    

#@receiver(pre_save, sender=Resource)
@receiver(pre_save, sender=User)
def model_pre_save(*args, **kwargs):
    print('pre_save')
    print("(args:{})".format(",".join(map(repr, args))))
    print("(kwargs.keys:{})".format(",".join(map(repr, kwargs.keys()))))
    print("(kwargs.values:{})".format(",".join(map(repr, kwargs.values()))))
    #print('Saving: {}'.format(kwargs['instance'].__dict__))


