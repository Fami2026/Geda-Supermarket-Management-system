from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Order 
from .models import Product


class Orderform(ModelForm):
	class Meta:
		model = Order
		fields ='__all__'

class SearchForm(ModelForm):
	class Meta:
		model =Product
		fields=['category','name']



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

