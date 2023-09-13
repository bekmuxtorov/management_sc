from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


@admin.register(models.StudyCenter)
class StudyCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',
                    'director', 'region', 'status')
    ordering = ('name', '-created_at')
    search_fields = ('name', 'description',
                     "director", 'region')
    list_filter = ("director__full_name", 'region', 'district')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_group_count',
                    'get_student_count', 'get_teacher_count')
    ordering = ('-created_at',)
    search_fields = ('name', )

    def get_group_count(self, obj):
        return obj.subject_groups.count()

    def get_student_count(self, obj):
        return obj.student_user.count()

    def get_teacher_count(self, obj):
        return obj.teacher_user.count()


@admin.register(models.SubjectGroup)
class SubjectGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'study_center', 'subject', 'teacher',
                    'get_students_count', 'price', 'room', 'study_day', 'status')
    ordering = ('-created_at', 'price', )
    list_filter = ('study_center', 'subject', 'room', 'study_day', 'status')
    search_fields = ('name', 'study_center', 'teacher',
                     'subject', 'price', 'room', 'study_day')

    def get_students_count(self, obj): return obj.students.count()


@admin.register(models.Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


@admin.register(models.StudyDay)
class StudyDayAdmin(admin.ModelAdmin):
    list_display = ('day', 'time', 'get_groups_count')
    search_fields = ('day', 'time')
    list_filter = ('day', 'time')

    def get_groups_count(self, obj): return obj.subject_groups.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('study_center', 'room_number', 'teacher',
                    'room_size', 'get_groups_count')
    ordering = ('study_center', 'room_size')
    list_filter = ('study_center',)

    def get_groups_count(self, obj): return obj.subject_groups.count()
    get_groups_count.short_description = _('Groups count')
