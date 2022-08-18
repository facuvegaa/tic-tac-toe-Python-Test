from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
BOARD = [[None,None,None],[None,None,None],[None,None,None]]
class Game(models.Model):
    player1 = ArrayField(models.CharField(max_length=25), size = 2,)
    player2 = ArrayField(models.CharField(max_length=25), size = 2,)
    next_turn = models.CharField(max_length=25)
    movements_played = models.IntegerField(default=0)
    winner = models.CharField(max_length=25, null=True, default="")
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=25, blank=True),
            size=3, blank=True
        ),
        size=3, default=BOARD
    )
    is_finished = models.BooleanField(default=False)
    

