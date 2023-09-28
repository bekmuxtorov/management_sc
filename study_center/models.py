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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Study center')
        verbose_name_plural = f"1.{_('Study centers')}"


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

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = f"3.{_('Subject')}"


class SubjectGroup(models.Model):
    study_center = models.ForeignKey(
        to=StudyCenter,
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='subject_groups'
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_('Name')
    )
    teacher = models.ForeignKey(
        to='account.TeacherUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('Teacher'),
        related_name='subject_groups'
    )
    students = models.ManyToManyField(
        to='account.StudentUser',
        related_name='subject_groups',
    )
    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        verbose_name=_('Subject'),
        related_name='subject_groups'
    )
    price = models.FloatField(
        verbose_name=_('Price'),
        blank=True,
        null=True
    )
    room = models.ForeignKey(
        to='study_center.Room',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='subject_groups'
    )
    study_day = models.ForeignKey(
        to='study_center.StudyDay',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='subject_groups'
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
    start_at = models.DateField(verbose_name=_('Start at'), auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return ' | '.join([self.name, self.teacher.full_name])

    class Meta:
        verbose_name = _('Study Group')
        verbose_name_plural = f"2.{_('Study Groups')}"


class Time(models.Model):
    study_center = models.ForeignKey(
        to=StudyCenter,
        on_delete=models.CASCADE,
        related_name='times',
        verbose_name=_("Study center"),
        blank=True,
        null=True
    )
    name = models.CharField(_('Name'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Time")
        verbose_name_plural = f"4.{_('Times')}"


class Day(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Day")
        verbose_name_plural = f"5.{_('Days')}"


class StudyDay(models.Model):
    study_center = models.ForeignKey(
        to=StudyCenter,
        on_delete=models.CASCADE,
        related_name='study_day',
        verbose_name=_("Study center"),
        blank=True,
        null=True
    )
    day = models.ForeignKey(
        to='study_center.Day',
        on_delete=models.CASCADE,
        verbose_name=_('Day'),
        related_name='study_day'
    )
    time = models.ForeignKey(
        to='study_center.Time',
        on_delete=models.CASCADE,
        verbose_name=_('Time')
    )

    def __str__(self):
        return ' | '.join([self.day.name, self.time.name])

    class Meta:
        verbose_name = _("StudyDay")
        verbose_name_plural = f"6.{_('Study Days')}"


class Room(models.Model):
    study_center = models.ForeignKey(
        to=StudyCenter,
        on_delete=models.CASCADE,
        verbose_name=_('Study Center'),
        related_name='rooms'
    )
    room_number = models.CharField(_('Room number'), max_length=50)
    room_size = models.IntegerField(_('Room size'))
    teacher = models.ForeignKey(
        to='account.TeacherUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_('Teacher'),
        related_name='rooms'
    )

    def __str__(self):
        return ' | '.join([self.room_number, self.teacher.user.full_name, str(self.study_center.name)])

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = f"7.{_('Rooms')}"
