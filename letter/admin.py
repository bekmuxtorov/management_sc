from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'get_contact_count')
    search_fields = ('type',)

    def get_contact_count(self, obj): return obj.contacts.count()
    get_contact_count.short_description = _('Contact count')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'study_center', 'contact')
    list_filters = ('type', 'study_center')
    ordering = ('-create_at', 'id')
    search_fields = ('user', 'study_center', 'contact')


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reveiver', 'study_center', 'is_read')
    ordering = ('-create_at',)
    search_fields = ('sender', 'reveiver', 'study_center', 'message')
