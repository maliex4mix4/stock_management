from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.

""" class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk}) """

class MyUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_attendant = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("User")

    def __str__(self):
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    """ 
    ADD_BY = (
        ('Pack', 'Pack'),
        ('Sachet', 'Sachet'),
        ('Sack', 'Sack'),
    ) 
    """
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Products_detail", kwargs={"pk": self.pk})




class Role(models.Model):
    name = models.CharField(max_length=500)
    group = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Role")
        verbose_name_plural = ("Roles")

    def __str__(self):
        return f"{self.name} --- {self.group}"

    def get_absolute_url(self):
        return reverse("Role_detail", kwargs={"pk": self.pk})


class UserRole(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("UserRole")
        verbose_name_plural = ("UserRoles")

    def __str__(self):
        return f"{self.role.name}"

    def get_absolute_url(self):
        return reverse("UserRole_detail", kwargs={"pk": self.pk})


class Activity(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Activity")
        verbose_name_plural = ("Activities")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Activity_detail", kwargs={"pk": self.pk})

class ManageUnit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'ManageUnit'
        verbose_name_plural = 'ManageUnits'


class Order(models.Model):
    """ 
    ADD_BY = (
        ('Pack', 'Pack'),
        ('Sachet', 'Sachet'),
        ('Sack', 'Sack'),
    ) 
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit = models.ForeignKey(ManageUnit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.unit.name}"

    def get_total(self):
        total = self.quantity * self.unit.price
        return total

    #def get_total_item_price(self):
    #   return self.quantity * self.product.price

    def get_absolute_url(self):
        return reverse("Order_Product_detail", kwargs={"pk": self.pk})

    # def save(self, *args, **kwargs):
    #    price = self.price
    #    price = self.product.price
    #    super().save(*args, **kwargs)


class OrderProduct(models.Model):
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    hold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = ("OrderProduct")
        verbose_name_plural = ("OrderProducts")

    def __str__(self):
        return self.ref_no
    '''
    def get_total(self):
        total = 0
        for order_item in self.orders.all():
            total += order_item.get_total_item_price()
        return total
    '''
    def get_absolute_url(self):
        return reverse("OrderProduct_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.ref_no =  self.orders.id
        super().save(*args, **kwargs)

