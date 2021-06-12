from django.db import models


class Team(models.Model):
    """
        Team model class
    """
    name = models.CharField(max_length=128, unique=True)


class Player(models.Model):
    """
        Player model class
    """
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=32)
    nation = models.CharField(max_length=64)

    team = models.ForeignKey(
        Team,
        related_name='players',
        on_delete=models.deletion.CASCADE
    )
