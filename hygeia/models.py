from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Pharmacy(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	pharmacy_name = models.CharField(max_length=200)
	logo = models.ImageField(upload_to='wopharm/pharmacy/logo', null=True, blank=True)
	digital_address = models.CharField(max_length=300)
	registration_code = models.CharField(max_length=100)
	region = models.CharField(max_length=50)


	class Meta:
		verbose_name_plural = 'pharmacies'


	def __str__(self):
		return self.pharmacy_name




class DrugCategory(models.Model):
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
	drug_class = models.CharField(max_length=100)
	general_description = models.TextField()


	class Meta:
		verbose_name_plural = 'Drug Categories'

	def __str__(self):
		return self.drug_class



class Drug(models.Model):
	category = models.ForeignKey(DrugCategory, on_delete=models.CASCADE)
	drug_name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=65, decimal_places=2)
	discount_percentage = models.DecimalField(max_digits=65, decimal_places=2, null=True, blank=True)
	expiry_date = models.DateField()
	image = models.ImageField(upload_to='wopharm/drugs/images')
	quantity_in_stock = models.PositiveIntegerField()
	description = models.CharField(max_length=200)
	side_effect = models.TextField()
	apply_discount = models.BooleanField(default=False)
	is_in_stock = models.BooleanField(default=False)
	publish = models.BooleanField(default=False)


	def __str__(self):
		return self.drug_name

	def get_pharmacy(self):
		return self.category.pharmacy


	def save(self, *args, **kwargs):
		if self.apply_discount == True:
			self.price = (self.price) - (self.price * self.discount_percentage / 100)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('drug-details', kwargs={'pk':self.pk})



class Precriptions(models.Model):
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
	drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
	created_on = models.DateField()
	prescribed_by = models.CharField(max_length=100)
	precribed_to = models.CharField(max_length=1000)
	precribed_for = models.TextField()
	dosage = models.CharField(max_length=300)
	relevant_advice = models.TextField()

	class Meta:
		verbose_name_plural = 'prescriptions'

	def __str__(self):
		return self.drug