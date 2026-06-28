from django.db import models
class Player(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    team=models.CharField(max_length=100)
    bio=models.TextField()