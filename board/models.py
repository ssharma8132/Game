from django.db import models

from django.db import models
from django.db.models import Count


class Game(models.Model):
    username = models.CharField(max_length=40)
    match = models.CharField(max_length=20)
    kill = models.PositiveIntegerField(default=0)
    time = models.TimeField(null=True)

    def save(self, *args, **kwargs):
        try:
            self.score = self.kill * 50
        except TypeError:
            pass
        super(Game, self).save(*args, **kwargs)
    score = models.PositiveIntegerField(null=True,editable=False)

    def rank(self):
        aggregate = Game.objects.filter(score__gt=self.score).order_by('last_name').aggregate(rank=Count('score'))
        return aggregate['rank'] + 1


    def __str__(self):
        return self.match
