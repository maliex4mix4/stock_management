from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import MyUser
from app.models import *  

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


