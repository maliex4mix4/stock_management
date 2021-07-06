from django.contrib import admin
from app.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from app.forms import MyUserCreationForm, MyUserChangeForm


# Register your models here.


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['username', 'is_admin', 'is_attendant']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_admin', 'is_attendant')}),
    ) #this will allow to change these fields in admin module


admin.site.register(MyUser, MyUserAdmin)

admin.site.register(Product)
#admin.site.register(User)
admin.site.register(Role)
admin.site.register(Activity)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Category)
admin.site.register(UserRole)
admin.site.register(ManageUnit)