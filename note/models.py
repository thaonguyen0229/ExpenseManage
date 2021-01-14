from django.db import models
from django.contrib.auth.models import User
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_spend = 0
    total_earn = 0

'''

class Spending(models.Model):
    amount = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField()
    #user = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Earning(models.Model):
    amount = models.IntegerField()
    description = models.TextField()
    create_date = models.DateTimeField()
    #user = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Repeat_event(models.Model):
    amount = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField()