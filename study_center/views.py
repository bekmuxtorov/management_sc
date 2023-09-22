from django.shortcuts import render
from rest_framework import generics

from . import serializers
from . import models


# Subject


# Subject Create API View
class SubjectCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


# Subject List API View
class SubjectListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


# Subject Detail API View
class SubjectDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Subject
    serializer_class = serializers.SubjectSerializer


# Subject Update API View
class SubjectUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


# Subject Delete API View
class SubjectDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


# StudyCenter


# StudyCenter Create API View
class StudyCenterCreateAPIVIew(generics.CreateAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer


# StudyCenter List API View
class StudyCenterListAPIView(generics.ListAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer


# StudyCenter Detail API View
class StudyCenterDetailAPIView(generics.RetrieveAPIView):
    queryset = models.StudyCenter
    serializer_class = serializers.StudyCenterSerializer


# StudyCenter Update API View
class StudyCenterUpdateAPIView(generics.UpdateAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer


# StudyCenter Delete API View
class StudyCenterDeleteAPIView(generics.DestroyAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer


# SubjectGroup


# SubjectGroup Create API View
class SubjectGroupCreateAPIVIew(generics.CreateAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer


# SubjectGroup List API View
class SubjectGroupListAPIView(generics.ListAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer


# SubjectGroup Detail API View
class SubjectGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = models.SubjectGroup
    serializer_class = serializers.SubjectGroupSerializer


# SubjectGroup Update API View
class SubjectGroupUpdateAPIView(generics.UpdateAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer


# SubjectGroup Delete API View
class SubjectGroupDeleteAPIView(generics.DestroyAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer


# StudyDay


# StudyDay Create API View
class StudyDayCreateAPIVIew(generics.CreateAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer


# StudyDay List API View
class StudyDayListAPIView(generics.ListAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer


# StudyDay Detail API View
class StudyDayDetailAPIView(generics.RetrieveAPIView):
    queryset = models.StudyDay
    serializer_class = serializers.StudyDaySerializer


# StudyDay Update API View
class StudyDayUpdateAPIView(generics.UpdateAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer


# StudyDay Delete API View
class StudyDayDeleteAPIView(generics.DestroyAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer

# Time


# Time Create API View
class TimeCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


# Time List API View
class TimeListAPIView(generics.ListAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


# Time Detail API View
class TimeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Time
    serializer_class = serializers.TimeSerializer


# Time Update API View
class TimeUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


# Time Delete API View
class TimeDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


# Day


# Day Create API View
class DayCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer


# Day List API View
class DayListAPIView(generics.ListAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer


# Day Detail API View
class DayDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Day
    serializer_class = serializers.DaySerializer


# Day Update API View
class DayUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer


# Day Delete API View
class DayDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer


# Room


# Room Create API View
class RoomCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


# Room List API View
class RoomListAPIView(generics.ListAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


# Room Detail API View
class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Room
    serializer_class = serializers.RoomSerializer


# Room Update API View
class RoomUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


# Region Delete API View
class RoomDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
