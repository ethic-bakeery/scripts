from django.db import models

# Create your models here.
class chat(models.Model):
    firstname   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    phonenumber = models.IntegerField(null=True)
    join_date   = models.DateField(null=True)


