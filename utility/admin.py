from django.contrib import admin
from.models import Utilities, Warehouse, GroupType, Product, UsageType

class UtilitiesAdmin(admin.ModelAdmin):
    list_display = ('utility_name',)

class wareHouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_code', 'warehouse_name', 'phone_number', 'address')

class GroupTypeAdmin(admin.ModelAdmin):
    list_display = ('group_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_code',
        'product_name',
        'product_abbreviation_code',
        'product_unit',
        'product_group',
        'product_place',
        'buy_price',
        'sell_price',
        'registration_date',
        'usage_type',
        'description'
    )

class UsageTypeAdmin(admin.ModelAdmin):
    list_display = ('usage_type',)
    

admin.site.register(Utilities, UtilitiesAdmin)
admin.site.register(Warehouse, wareHouseAdmin)
admin.site.register(GroupType, GroupTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UsageType, UsageTypeAdmin)