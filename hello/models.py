from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Player(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    position  = models.CharField(max_length = 50)
    age = models.PositiveSmallIntegerField()
    team = models.CharField(max_length=50)
    contract_date = models.DateField(auto_now = True, auto_now_add = False)