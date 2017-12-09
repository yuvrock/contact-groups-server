from django.contrib import admin
from  .models import *

# Register your models here.

class ContactsAdm(admin.ModelAdmin):
    list_display = ('name',)

class GroupAdm(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Contact, ContactsAdm)
admin.site.register(Group, GroupAdm)