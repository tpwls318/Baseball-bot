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




    def __unicode__(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)


class Pitcher(Player):
    pit_hand = models.CharField(max_length = 50) #ex) right handed, left handed
    kinds = models.CharField(max_length=50) #ex) starting pitcher, relief pitcher, closer, (winning pither)
    era = models.DecimalField(max_digits=4, decimal_places=2) #earned run average ---number like 2.17-how?-
    w = models.PositiveSmallIntegerField() #wins
    l = models.PositiveSmallIntegerField() #loses
    sv = models.PositiveSmallIntegerField() #saves
    k9 = models.DecimalField(max_digits=4, decimal_places=2)  #Strikeouts Per Nine innings  ex ) 10.83 , 7.58

    def show_statistics(self):
        return u'first name:{first_name}\tlast name:{last_name}\tposition:{position}\tage =:{age}\tteam:{team}\tHand:{pit_hand}\tKinds:{kinds}\tera:{era}\tw:{w}\tl:{l}\tsv:{sv}\tk9:{k9}'.format(first_name=self.first_name,last_name=self.last_name, position = self.position, age=self.age, team=self.team, pit_hand=self.pit_hand, kinds=self.kinds,era=self.era, w=self.w, l=self.l, sv=self.sv, k9=self.k9)

        #  def show_statistics(self):
       # return u'Hand:{pit_hand}\tKinds:{kinds}'.format(first_name=self.first_name,last_name=self.last_name, position = self.position, age=self.age, team=self.team, contract_date=self.contract_date , pit_hand=self.pit_hand, kinds=self.kinds,
                                                       # era=self.era, w=self.w, l=self.l, sv=self.sv, k9=self.k9)

class Hitter(Player):
    hit_hand = models.CharField(max_length=50)  # ex) right handed, left handed
    avg = models.DecimalField(max_digits=4, decimal_places=3)  # Batting Average ---number like 0.333-how?-
    obp = models.DecimalField(max_digits=4, decimal_places=3)  # On-base Percentage ---number like 0.413-how?-
    hr = models.PositiveSmallIntegerField()  #Homeruns
    rbi = models.PositiveSmallIntegerField()  # Runs Batted In
    r = models.PositiveSmallIntegerField()  # Runs

    def show_statistics(self):
        return u'first name:{first_name}\tlast name:{last_name}\tposition:{position}\tage =:{age}\tteam:{team}\tHand:{hit_hand}\tavg:{avg}\tobp:{obp}\thr:{hr}\trbi:{rbi}\tr:{r}'.format(
           first_name=self.first_name, last_name=self.last_name, position=self.position, age=self.age, team=self.team,
             hit_hand=self.hit_hand, avg=self.avg, obp=self.obp, hr=self.hr, rbi=self.rbi,
           r=self.r)


    # create tuple of Player table : player = Player.objects.create(first_name='Shinsoo',last_name='Choo',position='outfielder',age=35,team='Texas')
    # create tuple of Pitcher table : player = Pitcher.objects.create(first_name='Huynjin',last_name='Ryu',position='pitcher',age=32,team='Los Angeles'
    # + pit_hand = 'right handed', kinds = 'relief pitcher', era = 1.13, w = 9, l = 1, sv = 2, k9 = 10.83)
    # create tuple of Hitter table : player = Hitter.objects.create(first_name='Shinsoo',last_name='Choo',position='outfielder',age=35,team='Texas' ,
    # + hit_hand = 'right handed', avg = 0.333, obp = 0.413, hr = 20, rbi = 40, r = 70)
