"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.login, name='user_login'),
    path("home", views.login, name='user_login'),
    path('logout', views.Logout, name='user_logout'),


    path('administrator/', include(([
        path('dashboard', views.AdminDashboard, name='dashboard'),

        path('updateproduct', views.UpdateProduct, name='update_products'),
        path('viewproducts', views.ViewProduct, name='view_products'),
        path('addproduct', views.AddProduct, name='add_products'),
        path('deleteproduct/<int:pk>', views.DeleteProduct, name='delete_products'),

        path('updateuser', views.UpdateUser, name='update_user'),
        path('viewusers', views.ViewUser, name='view_users'),
        path('adduser', views.AddUser, name='add_user'),

        path('updateorder', views.UpdateOrder, name='update_order'),
        path('vieworders', views.ViewOrder, name='view_orders'),
        path('addorder', views.AddOrder, name='add_order'),

        path('productcategory', views.ProductCategory, name='category'),
        path('viewcategory', views.ViewProductCategory, name='view_categories'),
        path('deletecategory/<int:pk>', views.DeleteCategory, name='delete_category'),

        path('make_sales', views.MakeSales, name='sales'),

        


    ], 'app'), namespace='administrator')),


    path('attendant/', include(([
        path('dashboard', views.AttendantDashboard, name='dashboard'),

    ], 'app'), namespace='attendant')),
]
