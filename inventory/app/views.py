from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import  auth, messages
from django.contrib.auth import logout as django_logout
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.decorators import admin_required, attendant_required
from app.forms import *
from app.models import *

# Create your views here.
def login(request):
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            if form.is_valid():
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)

                    if request.user.is_admin:
                        return redirect('administrator:dashboard')
                    elif request.user.is_attendant:
                        return redirect('administrator:sales')
             

            else:
                args = {'form': form}
                messages.info(request, 'Invalid login credentials')
                return render(request, 'login.html', args)
        else:
            form = AuthenticationForm
        args = {'form': form}
        return render(request, 'login.html', args)

def Logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')

@login_required
def AdminDashboard(request):
    template_name = 'admindashboard.html'
    return render(request, template_name)

def AttendantDashboard(request):
    template_name = 'attendantdashboard.html'
    return render(request, template_name)


@admin_required
def AddProduct(request):
    template_name = 'addproduct.html'
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            b = form.save(commit=False)
            b.user = request.user
            b.save()
            messages.info(request, 'Item Added Successfully')
            return redirect('administrator:view_products')
    
    context = {
        'form': form,
    }
    return render(request, template_name, context)

@admin_required
def UpdateProduct(request):
    template_name = 'updateproduct.html'
    return render(request, template_name)

@admin_required
def ViewProduct(request):
    template_name = 'viewproduct.html'
    products = Product.objects.all()

    if request.method == 'POST':
        name = request.POST['product_name']
        category = request.POST['product_category_name']
        quantity = request.POST['product_quantity']
        price = request.POST['product_price']
        sold = request.POST['product_sold']
        unit = request.POST['product_unit']

        Product.objects.create(
            name=name,
            category=category,
            quantity=quantity,
            price=price,
            sold=sold,
            unit=unit
        )
    context = {
        'products': products
    }
    return render(request, template_name, context)

@admin_required
def DeleteProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('administrator:view_products')

@admin_required
def AddUser(request):
    template_name = 'adduser.html'
    form = MyUserCreationForm()
    if request.method== 'POST':
        form = MyUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'User Added Successfully')
            return redirect('administrator:view_users')


    
    context = {'form': form}
    return render(request, template_name, context)

@admin_required
def UpdateUser(request):
    template_name = 'updateuser.html'
    return render(request, template_name)

@admin_required
def ViewUser(request):
    template_name = 'viewusers.html'
    users = MyUser.objects.all()
    context = {'users': users}
    return render(request, template_name, context)

@admin_required
def AddOrder(request):
    template_name = 'addorder.html'
    return render(request, template_name)

@admin_required
def UpdateOrder(request):
    template_name = 'updateorder.html'
    return render(request, template_name)

@admin_required
def ViewOrder(request):
    template_name = 'vieworders.html'
    return render(request, template_name)

@admin_required
def ProductCategory(request):
    template_name = 'category.html'
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, template_name, context)

@admin_required
def ViewProductCategory(request):
    template_name = 'viewcategory.html'
    category = Category.objects.all()
    context = {'category': category}
    return render(request, template_name, context)


@admin_required
def DeleteCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('administrator:view_categories')


    
def MakeSales(request):
    template_name = 'makesales.html'
    return render(request, template_name)