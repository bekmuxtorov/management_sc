from django.db import models
from django.utils.translation import gettext_lazy as _


class StudyCenter(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50
    )
    description = models.CharField(
        verbose_name=_('Desctription'),
        max_length=200,
    )
    director = models.ForeignKey(
        to="account.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Director'),
        related_name='study_centers'
    )
    region = models.ForeignKey(
        to="account.Region",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='study_centers',
        verbose_name=_('Region')
    )
    district = models.ForeignKey(
        to="account.District",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='study_centers',
        verbose_name=_('District')
    )
    status = models.BooleanField(
        default=True,
        verbose_name=_('Status')
    )
    created_at = models.DateTimeField(
        verbose_name=_('Date of creation'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Update profile'),
        auto_now=True,
        blank=True,
        null=True
    )


class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Name')
    )
    created_at = models.DateTimeField(
        verbose_name=_('Date of creation'),
        auto_now_add=True
    )

    def __str__(self):
        return self.name
