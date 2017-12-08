from django.contrib import admin

from server import models


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ContactNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)


admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.ContactNumber, ContactNumberAdmin)
