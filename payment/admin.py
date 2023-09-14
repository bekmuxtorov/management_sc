from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.Season)
class Season(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.PaymetType)
class PaymetType(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(models.Discount)
class Discount(admin.ModelAdmin):
    list_display = ('name', 'study_center', 'type', 'value',
                    'start_date', 'end_date', 'status')
    search_fields = ('name', 'study_center', 'value')
    list_filter = ('type', 'status')


@admin.register(models.Billing)
class Billing(admin.ModelAdmin):
    list_display = ('student', 'study_center', 'study_group',
                    'month', 'payment_type', 'price', 'is_billing', 'payment_date')
    ordering = ('payment_date', 'month')
    list_filter = ('study_center', 'study_group',
                   'month', 'payment_type', 'is_billing')
