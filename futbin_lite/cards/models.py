from django.db import models


# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    nation = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    position = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.position})"


class PlayerCard(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    position = models.CharField(max_length=10)
    club = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    pace = models.IntegerField()
    shooting = models.IntegerField()
    passing = models.IntegerField()
    dribbling = models.IntegerField()
    defending = models.IntegerField()
    physical = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.rating})'


