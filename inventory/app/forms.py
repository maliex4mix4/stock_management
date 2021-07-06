from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import MyUser
from app.models import *  
from django.forms.models import inlineformset_factory
from django.forms import (formset_factory, modelformset_factory)

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'is_admin', 'is_attendant')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'is_admin', 'is_attendant')

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "slug", "user", 'sold')

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        exclude = ("created_at", "updated_at", 'slug')


class OrderProductForm(forms.ModelForm):

    #date_purcahse  = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'})) 
    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at']

OrderFormSet = formset_factory(OrderProductForm, extra=1)

class ManageUnitForm(forms.ModelForm):
    
    class Meta:
        model = ManageUnit
        exclude = ['created_at', 'updated_at', 'product']


