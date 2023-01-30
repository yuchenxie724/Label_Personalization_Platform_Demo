from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 120)
	labels = models.CharField(max_length = 120)
	#labels = models.TextField(blank = True, null = True)