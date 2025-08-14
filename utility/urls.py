from django.urls import path
from . import views

urlpatterns = [
    path("", views.master, name="master-page"),
    path("basic_informations/", views.main, name="main"),

    # Utility CRUD operations
    path("basic_informations/utilities/", views.AddUtility.as_view(), name="utilities"),
    path('basic_informations/utilities/delete/<int:pk>/', views.UtilityDelete.as_view(), name='delete-utility'),
    path("basic_informations/utilities/update/<int:pk>/", views.UtilityUpdate.as_view(), name="utility-update"),

    # Warehouses CRUD operatoinos
    path('basic_informations/warehouses/', views.WarehouseAdd.as_view(), name="warehouses"),
    path('basic_informations/warehouses/delete/<int:pk>/', views.WarehouseDelete.as_view(), name='warehouse-delete'),
    path("basic_informations/warehouses/update/<int:pk>/", views.WarehouseUpdate.as_view(), name="warehouse-update"),

    # Group Type CRUD operations
    path('basic_informations/groups', views.GroupeTypeAdd.as_view(), name='group-types'),
    path('basic_informations/groups/delete/<int:pk>', views.GroupTypeDelete.as_view(),name='group-types-delete'),
    path('basic_informations/groups/update/<int:pk>', views.GroupTypeUpdate.as_view(), name="group-types-update"),

    # Product CRUD operations
    path('basic_informations/products/', views.ProductAdd.as_view(), name='products'),
    path('basic_informations/products/delete/<int:pk>', views.ProductDelete.as_view(), name="product-delete"),
    path('basic_informations/products/update/<int:pk>', views.ProductUpdate.as_view(), name="product-update"),

    # Usage Type CRUD operations
    path("basic_informations/usagetype/", views.UsageTypeAdd.as_view(), name='usage-type'),
    path("basic_informations/usagetype/delete/<int:pk>", views.UsageTypeDelete.as_view(), name="usage-type-delete"),
    path("basic_informations/usagetype/update/<int:pk>", views.UsageTypeUpdate.as_view(), name="usage-type-update"),
]
