from django.db import models
from django.utils.translation import gettext_lazy as _


DISCOUNT_TYPE = (
    ('percentage', _('Percentage')),
    ('money', _('Money'))
)


class Season(models.Model):
    name = models.CharField(_('Month'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Season')
        verbose_name_plural = f"4.{_('Seasons')}"


class PaymetType(models.Model):
    name = models.CharField(_('Type'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('PaymetType')
        verbose_name_plural = f"3.{_('PaymetTypes')}"


class Discount(models.Model):
    study_center = models.ForeignKey(
        to="study_center.StudyCenter",
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='discount'
    )
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'))
    type = models.CharField(
        verbose_name=_('Type'),
        choices=DISCOUNT_TYPE,
        default='percentage',
        max_length=10
    )
    value = models.IntegerField(_('Value'))
    start_date = models.DateField(_('start_date'), auto_now=True)
    end_date = models.DateField(_('end_date'), auto_now=True)
    status = models.BooleanField(_('Status'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = f"2.{_('Discounts')}"


class Billing(models.Model):
    study_center = models.ForeignKey(
        to="study_center.StudyCenter",
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='billings'
    )
    study_group = models.ForeignKey(
        to="study_center.SubjectGroup",
        on_delete=models.CASCADE,
        verbose_name=_('Study Group'),
        related_name='billings'
    )
    student = models.ForeignKey(
        to="account.StudentUser",
        on_delete=models.CASCADE,
        verbose_name=_('Student'),
        related_name='billings'
    )
    month = models.ForeignKey(
        to=Season,
        on_delete=models.CASCADE,
        verbose_name=_('Month'),
        related_name='billings'
    )
    payment_type = models.ForeignKey(
        to=PaymetType,
        on_delete=models.CASCADE,
        verbose_name=_('Payment Type'),
        related_name='billings'
    )
    discount = models.ForeignKey(
        to=Discount,
        on_delete=models.CASCADE,
        verbose_name=_('Discount'),
        related_name='billings',
        null=True,
        blank=True
    )
    price = models.FloatField(_('Price'))
    is_billing = models.BooleanField(_('Is Billing'), default=True)
    comment = models.CharField(_('Comment'), max_length=100)
    payment_date = models.DateField(_('Payment Date'), auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.full_name

    class Meta:
        verbose_name = _('Billing')
        verbose_name_plural = f"1.{_('Billings')}"
