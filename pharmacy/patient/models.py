from django.db import models
from hygeia.models import Drug, Pharmacy
from django.contrib.auth import get_user_model
from django.utils import timezone
from delivery.models import Delivery





user = get_user_model()
class PatientRecord(models.Model):
	patient = models.ForeignKey(user, on_delete=models.CASCADE)
	sex = models.CharField(max_length=10)
	age = models.PositiveIntegerField()
	brief_history = models.TextField()
	symptoms_description = models.TextField()

	def __str__(self):
		return self.patient.last_name


class Order(models.Model):
	item = models.ForeignKey(Drug, on_delete=models.CASCADE)
	date_created = models.DateField(default=timezone.now)
	created_by = models.ForeignKey(user, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)


	def __str__(self):
		return self.item.drug_name


class OrderItem(models.Model):
	item = models.ForeignKey(Order, on_delete=models.CASCADE)
	created_on = models.DateField(default=timezone.now)
	delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
	delivered = models.BooleanField(default=False)

	def __str__(self):
		return self.item.date_created