from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
#from django.contrib.auth.models import Group


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


class SmartUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salt = models.CharField(max_length=255)

    def __str__(self):
        return self.user.name


#@receiver(post_save, sender=Resource)
@receiver(post_save, sender=User)
def model_post_save(sender, instance, *args, **kwargs):
    smart_user = SmartUser(user=instance, salt='bla-bla-bla')
    smart_user.save()
    print('Saved: {}'.format(kwargs['instance'].__dict__))


@receiver(pre_save, sender=User)
@receiver(pre_save, sender=Resource)
def model_pre_save(sender, **kwargs):
    print('Saving: {}'.format(kwargs['instance'].__dict__))


#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#
#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#
#class SecurityGroup(models.Model):
#    group = models.OneToOneField(Group, on_delete=models.CASCADE)
#    custom_field = models.CharField(max_length=191)
#
#    def __str__(self):
#        return self.group.name
