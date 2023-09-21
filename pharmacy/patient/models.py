from django.db import models
from hygeia.models import Drug
from django.contrib.auth import get_user_model

user = get_user_model()

class PatientRecord(models.Model):
	patient = models.ForeignKey(user, on_delete=models.CASCADE)
	#drup_purchase = models.ForeignKey(Drug, on_delete=models.CASCADE)
	sex = models.CharField(max_length=10)
	age = models.PositiveIntegerField()
	brief_history = models.TextField()
	symptoms_description = models.TextField()


class OrderItem(models.Model):
	drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
	date_created = models.DateField()
