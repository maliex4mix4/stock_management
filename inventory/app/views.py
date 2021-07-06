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
            messages.info(request, 'Product Added Successfully')
            return redirect('administrator:view_products')
    
    context = {
        'form': form,
    }
    return render(request, template_name, context)

@admin_required
def UpdateProduct(request, pk):
    template_name = 'updateproduct.html'
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Product Updated Successfully')
            return redirect('administrator:view_products')
    context = {
        "form": form,
        "product": product
    }
    return render(request, template_name, context)

@admin_required
def ViewProduct(request):
    template_name = 'viewproduct.html'
    products = Product.objects.all().order_by('-created_at')
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            b = form.save(commit=False)
            b.user = request.user
            b.save()
            messages.info(request, 'Product Added Successfully')
            return redirect('administrator:view_products')

    context = {
        'products': products,
        'form': form,
    }
    return render(request, template_name, context)

@admin_required
def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.info(request, 'Product Deleted Successfully')
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
def UpdateUser(request, pk):
    template_name = 'updateuser.html'
    user = get_object_or_404(MyUser, pk=pk)
    form = MyUserCreationForm(instance=user)
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'User Updated Successfully')
            return redirect('administrator:view_users')
    context = {
        "form": form,
        "user": user
    }
    return render(request, template_name, context)

@admin_required
def ViewUser(request):
    template_name = 'viewusers.html'
    users = MyUser.objects.all().order_by('-date_joined')
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'User Added Successfully')
            return redirect('administrator:view_users')

    context = {
        'users': users,
        'form': form,
        }
    return render(request, template_name, context)


@admin_required
def DeleteUser(request, pk):
    user = MyUser.objects.get(id=pk)
    user.delete()
    messages.info(request, 'User Deleted Successfully')
    return redirect('administrator:view_users')


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
            messages.info(request, 'Category Added Successfully')
            return redirect('administrator:view_categories')
    context = {'form': form}
    return render(request, template_name, context)

@admin_required
def ViewProductCategory(request):
    template_name = 'viewcategory.html'
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.info(request, 'Category Added Successfully')
            return redirect('administrator:view_categories')

    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
        }
    return render(request, template_name, context)


@admin_required
def DeleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    messages.info(request, 'Category Deleted Successfully')
    return redirect('administrator:view_categories')



@admin_required
def UpdateProductCategory(request, pk):
    template_name = 'updatecategory.html'
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.info(request, 'Category Updated Successfully')
            return redirect('administrator:view_categories')
    context = {
        "form": form,
        "category": category
    }
    return render(request, template_name, context)


def MakeSales(request):
    template_name = 'makesales.html'
    order = OrderProductForm()
    order_item = OrderFormSet()
    
    if request.method == 'POST':
        order = OrderProductForm(request.POST or None)
        order_item = OrderFormSet(request.POST or None)

        if order.is_valid() and order_item.is_valid() :   
            print("Working Finesss World")         
            p = order.save(commit=False)
            #p.user = request.user
            p.save()    

            for image in order_item:
                myimage = image.cleaned_data.get('image')
                image = LandImage(land=p, image=myimage)
                image.save()

            messages.success(request, 'The Post Has been Added Successully!')
            return redirect('administrator:dashboard')
    
    
    
    product = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Product Updated Successfully')
            return redirect('administrator:view_products')
    context = {
        "order": order,
        "order_item": order_item
    }
    return render(request, template_name, context)

@admin_required
def ManageUnits(request, pk):
    template_name = 'manage_units.html'
    product = get_object_or_404(Product, pk=pk)
    units = ManageUnit.objects.filter(product = product)
    form = ManageUnitForm()
    if request.method == 'POST':
        form = ManageUnitForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.product = product
            f.save()
            messages.info(request, f'{f.name} Unit Added Successfully')
            return redirect('administrator:manageUnit', product.id )
    context = {
        'form': form,
        'product': product,
        'units': units,
        }
    return render(request, template_name, context)



@admin_required
def UpdateUnit(request, pk):
    template_name = 'updateunit.html'
    unit = get_object_or_404(ManageUnit, pk=pk)
    product = unit.product
    form = ManageUnitForm(instance=unit)
    if request.method == 'POST':
        form = ManageUnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            messages.info(request, f'{unit.name} Unit Updated Successfully')
            return redirect('administrator:manageUnit', product.id)
    context = {
        "form": form,
        "unit": unit
    }
    return render(request, template_name, context)

@admin_required
def DeleteUnit(request, pk):
    unit = ManageUnit.objects.get(id=pk)
    product = unit.product
    unit.delete()
    messages.info(request, f'{unit.name} Unit Deleted Successfully')
    return redirect('administrator:manageUnit', product.id)