from django.contrib import admin

# Register your models here.

from .models import Order, Parcel_size, Parcel_weight, Delivery_status

admin.site.register(Order)
admin.site.register(Parcel_size)
admin.site.register(Parcel_weight)
admin.site.register(Delivery_status)