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

class Pitcher(Player):
    pit_hand = models.CharField(max_length = 50) #ex) right handed, left handed
    kinds = models.CharField(max_length=50) #ex) starting pitcher, relief pitcher, closer, (winning pither)
    era = models.DecimalField(max_digits=4, decimal_places=2) #earned run average ---number like 2.17-how?-
    w = models.PositiveSmallIntegerField() #wins
    l = models.PositiveSmallIntegerField() #loses
    sv = models.PositiveSmallIntegerField() #saves
    k9 = models.DecimalField(max_digits=4, decimal_places=2)  #Strikeouts Per Nine innings  ex ) 10.83 , 7.58

class Hitter(Player):
    hit_hand = models.CharField(max_length=50)  # ex) right handed, left handed
    avg = models.DecimalField(max_digits=4, decimal_places=3)  # Batting Average ---number like 0.333-how?-
    obp = models.DecimalField(max_digits=4, decimal_places=3)  # On-base Percentage ---number like 0.413-how?-
    hr = models.PositiveSmallIntegerField()  #Homeruns
    rbi = models.PositiveSmallIntegerField()  # Runs Batted In
    r = models.PositiveSmallIntegerField()  # Runs

    # create tuple of Player table : player = Player.objects.create(first_name='Shinsoo',last_name='Choo',position='outfielder',age=35,team='Texas')
    # create tuple of Pitcher table : player = Pitcher.objects.create(first_name='Huynjin',last_name='Ryu',position='pitcher',age=32,team='Los Angeles'
    # + pit_hand = 'right handed', kinds = 'relief pitcher', era = 1.13, w = 9, l = 1, sv = 2, k9 = 10.83)
    # create tuple of Hitter table : player = Hitter.objects.create(first_name='Shinsoo',last_name='Choo',position='outfielder',age=35,team='Texas' ,
    # + hit_hand = 'right handed', avg = 0.333, obp = 0.413, hr = 20, rbi = 40, r = 70)
