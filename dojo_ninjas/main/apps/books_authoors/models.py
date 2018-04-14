from __future__ import unicode_literals

from django.db import models
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "<author object: {} {} {}>".format(self.first_name, self.last_name, self.email)


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, related_name="books")
    notes = models.TextField(default="some string")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "<book object: {} {} {}>".format(self.name, self.desc, self.author)

          


        



