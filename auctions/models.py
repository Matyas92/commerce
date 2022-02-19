from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import BinaryField
from django.forms.models import model_to_dict

from django.db.models.deletion import CASCADE

class User(AbstractUser):
    pass

class CreateListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    tags = models.ForeignKey('Tag', blank=True, on_delete=CASCADE)
    startingBid = models.IntegerField()
    url = models.URLField(max_length=500) 
    closing = models.BooleanField(default="False")
    currentbidder = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Watchlist(models.Model):
    userlist = models.ForeignKey(User, on_delete=CASCADE)
    element = models.ForeignKey(CreateListing, on_delete=CASCADE)

    def __str__(self):
        return str(self.element)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    listToComment = models.ForeignKey(CreateListing, on_delete=CASCADE)
    comment = models.CharField(max_length=150) 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    listToBid = models.ForeignKey(CreateListing, on_delete=CASCADE)
    bid = models.IntegerField()

    def __int__(self):
        return self.user + ' ' + self.bid
