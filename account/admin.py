from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from . import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'district_count', 'study_center_count')
    search_fields = ('name',)

    def district_count(self, obj):
        return obj.districts.count()

    def study_center_count(self, obj):
        return obj.study_centers.count()


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'study_center_count')
    search_fields = ('name', 'region__name')
    list_filter = ('region__name',)
    ordering = ('region__name',)

    def study_center_count(self, obj):
        return obj.study_centers.count()


@admin.register(models.User)
class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "phone_number",
        "type",
        "created_at",
        "is_phone_verified",
        "is_staff"
    )
    list_filter = ("is_staff", "is_superuser",
                   "groups", "type", "study_center")
    fieldsets = (
        (
            _("General data"),
            {
                "fields": (
                    "type",
                    "phone_number",
                    "full_name",
                    "passport_or_id",
                    "password_or_id_number"
                )
            },
        ),
        (
            _("Teachers"),
            {
                "fields": (
                    "study_center",
                    "subjects",
                    "salary_percentage"
                )
            },
        ),

        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser",
                        "groups", "user_permissions")},
        ),
        ("Important dates", {
         "fields": ("last_login", 'sms_code', 'is_phone_verified')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("type", "phone_number", "password1", "password2"),
            },
        ),
    )
    search_fields = ("phone_number", "full_name", "full_name")
    ordering = ("type",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.type = form.cleaned_data.get('type')
        super().save_model(request, obj, form, change)
