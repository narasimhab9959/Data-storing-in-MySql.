from django.db import models

# Create your models here.

class topic(models.Model):
    topic_name=models.CharField(max_length=100)


class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

