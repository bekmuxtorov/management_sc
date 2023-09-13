from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactType(models.Model):
    type = models.CharField(_('Type'), max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = _('Contact Type')
        verbose_name_plural = f"2.{_('Contact Types')}"


class Contact(models.Model):
    study_center = models.ForeignKey(
        to="study_center.StudyCenter",
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='contacts'
    )
    user = models.ForeignKey(
        to="account.User",
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name=_('User')
    )
    type = models.ForeignKey(
        to=ContactType,
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name=_('Type')
    )
    contact = models.CharField(_('Contact'), max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' | '.join([self.user, self.type])

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = f"3.{_('Contacts')}"


class Message(models.Model):
    study_center = models.ForeignKey(
        to="study_center.StudyCenter",
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='messages'
    )

    sender = models.ForeignKey(
        to="account.User",
        on_delete=models.CASCADE,
        related_name='sender_user',
        verbose_name=_('Sender')
    )
    reveiver = models.ForeignKey(
        to="account.User",
        on_delete=models.CASCADE,
        related_name='reveiver_user',
        verbose_name=_('Reveiver')
    )
    message = models.TextField(_('Message text'))
    create_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return ' -> '.join([str(self.sender), str(self.reveiver)])

    class Meta:
        verbose_name = 'Letter'
        verbose_name_plural = f"1.{_('Letters')}"
