from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import CustomManager



SEX = [
    ('Male', 'Male'),
    ('Female', 'Female')
    ]
    
class User(AbstractBaseUser):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	ghana_card_number = models.CharField(max_length=50)
	telephone = models.CharField(help_text='0597856551', max_length=20)
	gender = models.CharField(max_length=10, choices=SEX)
	age = models.PositiveIntegerField(default=0)
	has_a_pharmacy = models.BooleanField(verbose_name='Do you intend to create you online pharmacy store?', default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now) 

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = 	['telephone']

	objects = CustomManager()
#4445 6940 0253 8283
#485
#11/24

	def __str__(self):
		return f'{self.first_name} {self.last_name}'
	
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_staff(self):
		return self.is_admin
