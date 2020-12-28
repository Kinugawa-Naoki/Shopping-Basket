from django.contrib import admin
from .models import UserProfile, Shopping_ListNameModel, Shopping_ListModel
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Shopping_ListModel)
admin.site.register(Shopping_ListNameModel)