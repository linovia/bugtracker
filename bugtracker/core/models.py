from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.TextField()
    owner = models.ForeignKey('auth.User')


class Bug(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    state = models.CharField(max_length=16)
    project = models.ForeignKey(Project)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)


class BugComment(models.Model):
    bug = models.ForeignKey(Bug)
    content = models.TextField()
    owner = models.ForeignKey('auth.User')
    creation_date = models.DateTimeField(auto_now_add=True)


