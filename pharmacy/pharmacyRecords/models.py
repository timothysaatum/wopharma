from django.db import models
from hygeia.models import Drug


class Order(models.Model):
	drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
	