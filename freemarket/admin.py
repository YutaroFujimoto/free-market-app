from django.contrib import admin
from .models import Product
from .models import Userdata

# Register your models here.
admin.site.register(Product)
admin.site.register(Userdata)