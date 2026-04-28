from django.contrib import admin
from isbat.models import person,registrtaion
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=['name']

class RegistrationAdmin(admin.ModelAdmin):
    list_display=['code']

class ProdAdmin(admin.ModelAdmin):
    list_display=['prodname','productcat','prodyear']


admin.site.register(person,PersonAdmin)
admin.site.register(registrtaion,RegistrationAdmin)
admin.site.register(Products,ProdAdmin)
