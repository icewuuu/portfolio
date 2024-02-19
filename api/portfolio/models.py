from django.db import models

class Education(models.Model):
    school = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 50)
    years = models.CharField(max_length = 25)
    description = models.TextField()
    order = models.IntegerField()

class Work(models.Model):
    company = models.CharField(max_length = 50)
    years = models.CharField(max_length = 25)
    description = models.TextField()
    order = models.IntegerField()


class Certificates(models.Model):
    certificate = models.CharField(max_length = 50)
    years = models.CharField(max_length = 25)
    description = models.TextField()
    order = models.IntegerField()

class Portfolio(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    url = models.URLField()
    order = models.IntegerField()

