from django.db import models
from django.contrib.auth import get_user_model





user = get_user_model()


class Delivery(models.Model):
	created_by = models.ForeignKey(user, on_delete=models.CASCADE)
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name
