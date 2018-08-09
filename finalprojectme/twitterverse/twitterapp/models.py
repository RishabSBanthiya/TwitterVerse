from django.db import models
from datetime import datetime


class UEFA(models.Model):


    Teams = models.CharField(
        max_length=64,
    )

    def __str__(self):
        return f"{self.Teams}"
#-------------------------------------------------------------------------
class Following(models.Model):


    Username = models.CharField(
        max_length=64,
    )

    Phrases = models.CharField(
        max_length=64,
    )

    def __str__(self):
        return f"{self.Phrases}"

#-------------------------------------------------------------------------