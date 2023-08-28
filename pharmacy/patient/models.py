from django.db import models
from hygeia.models import Drug
from django.contrib.auth.models import User




class Patient(models.Model):
	patient = models.ForeignKey(User, on_delete=models.CASCADE)
	drup_purchase = models.ForeignKey(Drug, on_delete=models.CASCADE)
	sex = models.CharField(max_length=10)
	age = models.PositiveIntegerField()
	brief_history = models.TextField()
	symptoms_description = models.TextField()