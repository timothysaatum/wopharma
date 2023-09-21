from django import forms
from .models import Pharmacy


class PharmacyCreationForm(forms.ModelForm):
	
	class Meta:
		model = Pharmacy

		exclude = ('owner',)