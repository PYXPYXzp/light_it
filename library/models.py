from __future__ import unicode_literals

from django.db import models


class TabsMenu(models.Model):
    name_tabs = models.CharField(max_length=20)
    link_tabs = models.CharField(max_length=200)
    label_tabs = models.CharField(max_length=200)

    def __unicode__(self):
        return ''.join([self.name_tabs])


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return ''.join([self.first_name, self.last_name])


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return ''.join([self.first_name, self.last_name])


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    user_now = models.ForeignKey(User, blank=True, null=True)
    user_before = models.ManyToManyField(User,
                                         related_name='ex_user', blank=True)
    date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.title
