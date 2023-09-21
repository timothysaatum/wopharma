from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Zoppie'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Zigi'}))
	#gender = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Male'}))
	telephone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'E.g 0245867859'}),
        required=True)
	ghana_card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'GHA-XXXXXXXXX-X'}))
	age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'27'}))

	class Meta:
		model = User
		fields = ['email','first_name', 'last_name', 'telephone', 'ghana_card_number', 'age', 'gender', 'has_a_pharmacy', 'password1', 'password2']

