from django.contrib import admin

from django.contrib import admin

from .models import *

class FormAdmin(admin.ModelAdmin):
    list_display = ['name','email']

admin.site.register(Service)
admin.site.register(User)
admin.site.register(Price)
admin.site.register(Product)

