from django.db import models

# Create your models here.
class Landing_page_template(models.Model):
    heading = models.CharField(max_length=10)
    introduction = models.CharField(max_length=500, default='Your Introduction goes here')
