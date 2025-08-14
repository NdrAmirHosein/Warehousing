from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone

class Utilities(models.Model):
    utility_name = models.CharField("Utility Name", max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.utility_name

class Warehouse(models.Model):
    warehouse_code = models.IntegerField("Warehouse Code", unique=True, null=False, blank=False, primary_key=True)
    warehouse_name = models.CharField("Warehouse Name", max_length=50, null=False, blank=False)
    phone_number = models.CharField("Warehouse Phone Number", blank=True, null=True, max_length=20)
    address = models.CharField("Warehouse Address", max_length=150, null=True, blank=True)

    def __str__(self):
        return self.warehouse_name

class GroupType(models.Model):
    group_name = models.CharField("Group Type", max_length=50, null=False, blank=False)

    def __str__(self):
        return self.group_name


class UsageType(models.Model):
    usage_type = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.usage_type

class Product(models.Model):
    product_code = models.IntegerField("Product Code", unique=True, null=False, blank=False, primary_key=True)
    product_name = models.CharField("Product Name", max_length=50, null=False, blank=False)
    product_abbreviation_code = models.CharField("Abbreviation Code", max_length=20, blank=True)
    product_unit = models.ForeignKey(Utilities, on_delete=models.PROTECT)
    product_group = models.ForeignKey(GroupType, on_delete=models.PROTECT)
    product_place = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    buy_price = models.DecimalField("Product Buy Price", max_digits=15, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(Decimal('0.00'))])
    sell_price = models.DecimalField("Product Sell Price", max_digits=15, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(Decimal('0.00'))])
    registration_date = models.DateField("Date of Registration",default=timezone.now, blank=True, null=True)
    usage_type = models.ForeignKey(UsageType, on_delete=models.PROTECT)
    description = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return f"{self.product_name} ({self.product_code})"
