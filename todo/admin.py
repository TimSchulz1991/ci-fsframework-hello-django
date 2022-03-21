from django.contrib import admin
from .models import Item
# . so that we import from models in current directory

# Register your models here.

admin.site.register(Item)
