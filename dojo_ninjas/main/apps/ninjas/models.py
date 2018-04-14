from __future__ import unicode_literals

from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default='DEFAULT VALUE')
    def __repr__(self):
        return "<Dojos object: {} {} {} {}>".format(self.name, self.city, self.state, self.desc)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos, related_name="ninjas") 
    def __repr__(self):
        return "<Dojos object: {} {} {}>".format(self.first_name, self.last_name, self.dojo) 
