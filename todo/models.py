from __future__ import unicode_literals
from django.db import models

class TodoElements(models.Model):
	todo_text = models.CharField(max_length=200)
	done = models.BooleanField()