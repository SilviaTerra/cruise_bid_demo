from __future__ import unicode_literals

from django.db import models


class Cruise(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    numPlots = models.IntegerField(default=0)
    bid = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name
        
