from rest_framework import serializers

from . import models


class SubjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ('id', 'name')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'


class StudyCenterNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyCenter
        fields = ('id', 'name')


class StudyCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyCenter
        fields = '__all__'


class SubjectGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectGroup
        fields = '__all__'


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Time
        fields = '__all__'


class StudyDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudyDay
        fields = '__all__'


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Day
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = '__all__'
