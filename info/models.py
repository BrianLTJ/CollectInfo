from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.TextField(max_length=20)
	phone = models.TextField(max_length=12)
	qq = models.TextField(max_length=12)
	dorm = models.TextField(max_length=50)
	birthday = models.TextField(max_length=50)
	place = models.TextField(max_length=100)
