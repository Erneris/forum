from django.db import models

class post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 200)
    user = models.CharField(max_length = 15)
    category = models.CharField(max_length = 20)
    date = models.DateField()
