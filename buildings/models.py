from django.db import models


class MainPageData(models.Model):
    img_url = models.CharField(max_length=1280)
    text = models.TextField(max_length=500)
    email = models.EmailField()
    tel_no = models.CharField(max_length=20)


class ProjectsDone(models.Model):
    img_url = models.CharField(max_length=1280)
    text = models.TextField(max_length=500)