from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from django.utils.translation import gettext_lazy as _

from .managers import UserManager


# Create your models here.
USER_TYPE = (
    ('teacher', _('Teacher')),
    ('director', _('Director')),
    ('adminstrator', _('Adminstrator')),
    ('student', _('Student'))
)


DOCUMENT_TYPES = (
    ('passport', _('Passport')),
    ('document_id', _('ID'))
)


class Region(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100
    )

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100
    )
    region = models.ForeignKey(
        to=Region,
        on_delete=models.CASCADE,
        related_name='districts'
    )

    def __str__(self):
        return ' | '.join([self.name, self.region.name])


class User(AbstractBaseUser, PermissionsMixin):
    type = models.CharField(
        max_length=13,
        choices=USER_TYPE,
        default='teacher',
        verbose_name=_('User type')
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name=_('Full name')
    )
    phone_number = models.CharField(
        verbose_name=_('Phone number'),
        max_length=20,
        unique=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message=_(
                    'Invalid phone number. Please enter in the format +998901234567')
            ),
        ]
    )
    passport_or_id = models.CharField(
        choices=DOCUMENT_TYPES,
        default=_('passport'),
        max_length=11
    )
    password_or_id_number = models.CharField(
        verbose_name=_('Password or ID number'),
        max_length=15,
        blank=True
    )
    study_center = models.ForeignKey(
        to="study_center.StudyCenter",
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='users',
        blank=True,
        null=True
    )
    sms_code = models.IntegerField(
        verbose_name=_('SMS code'),
        blank=True,
        null=True
    )
    is_phone_verified = models.BooleanField(
        verbose_name=_('Is phone verified'),
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name=_("is staff"),
        default=False
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

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.full_name


class TeacherUser(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='teacher_user'
    )
    subject = models.ForeignKey(
        to="study_center.Subject",
        on_delete=models.CASCADE,
        related_name="teacher_user",
        blank=True,
        null=True
    )
    salary_percentage = models.FloatField(
        verbose_name=_('Salary percentage'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.full_name


class StudentUser(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='student_user'
    )
    subject = models.ForeignKey(
        to="study_center.Subject",
        on_delete=models.CASCADE,
        related_name="student_user",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.full_name
