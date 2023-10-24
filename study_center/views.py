from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from . import serializers
from . import models
from account import permissions as user_perm


# Subject


# Subject Create API View
class SubjectCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Subject List API View
class SubjectListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)


# Subject Detail API View
class SubjectDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Subject
    serializer_class = serializers.SubjectSerializer


# Subject Update API View
class SubjectUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Subject Delete API View
class SubjectDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# StudyCenter


# StudyCenter Create API View
class StudyCenterCreateAPIVIew(generics.CreateAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer
    permission_classes = [user_perm.IsDirector]


# StudyCenter List API View
class StudyCenterListAPIView(generics.ListAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer
    permission_classes = [user_perm.IsDirector]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('name', 'description')
    filterset_fields = ('region', 'district', 'status')


# StudyCenter Detail API View
class StudyCenterDetailAPIView(generics.RetrieveAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer
    permission_classes = [user_perm.IsDirector]


# StudyCenter Update API View
class StudyCenterUpdateAPIView(generics.UpdateAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# StudyCenter Delete API View
class StudyCenterDeleteAPIView(generics.DestroyAPIView):
    queryset = models.StudyCenter.objects.all()
    serializer_class = serializers.StudyCenterSerializer
    permission_classes = [user_perm.IsDirector]


# SubjectGroup


# SubjectGroup Create API View
class SubjectGroupCreateAPIVIew(generics.CreateAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# SubjectGroup List API View
class SubjectGroupListAPIView(generics.ListAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer
    permission_classes = [
        user_perm.IsDirectorOrAdminstrator | user_perm.IsTeacher
    ]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = (
        'study_center', 'teacher',
        'subject', 'room', 'study_day'
    )
    search_fields = (
        'name', 'study_center', 'price',
        'teacher__name', 'room__name', 'study_center__name'
    )


# SubjectGroup Detail API View
class SubjectGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = models.SubjectGroup
    serializer_class = serializers.SubjectGroupSerializer
    permission_classes = [
        user_perm.IsDirectorOrAdminstrator | user_perm.IsTeacher
    ]


# SubjectGroup Update API View
class SubjectGroupUpdateAPIView(generics.UpdateAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# SubjectGroup Delete API View
class SubjectGroupDeleteAPIView(generics.DestroyAPIView):
    queryset = models.SubjectGroup.objects.all()
    serializer_class = serializers.SubjectGroupSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# StudyDay


# StudyDay Create API View
class StudyDayCreateAPIVIew(generics.CreateAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# StudyDay List API View
class StudyDayListAPIView(generics.ListAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ('day__name', 'time__name', 'study_center__name')
    filterset_fields = ('day', 'time', 'day__name',
                        'time__name', 'study_center__name')


# StudyDay Detail API View
class StudyDayDetailAPIView(generics.RetrieveAPIView):
    queryset = models.StudyDay
    serializer_class = serializers.StudyDaySerializer


# StudyDay Update API View
class StudyDayUpdateAPIView(generics.UpdateAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# StudyDay Delete API View
class StudyDayDeleteAPIView(generics.DestroyAPIView):
    queryset = models.StudyDay.objects.all()
    serializer_class = serializers.StudyDaySerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Time


# Time Create API View
class TimeCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Time List API View
class TimeListAPIView(generics.ListAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ('name', 'study_center__name')
    filterset_fields = ('study_center__name',)


# Time Detail API View
class TimeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer


# Time Update API View
class TimeUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Time Delete API View
class TimeDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Time.objects.all()
    serializer_class = serializers.TimeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Day


# Day Create API View
class DayCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Day List API View
class DayListAPIView(generics.ListAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('name')


# Day Detail API View
class DayDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Day
    serializer_class = serializers.DaySerializer


# Day Update API View
class DayUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Day Delete API View
class DayDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Day.objects.all()
    serializer_class = serializers.DaySerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Room


# Room Create API View
class RoomCreateAPIVIew(generics.CreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Room List API View
class RoomListAPIView(generics.ListAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ('name', 'study_center', 'teacher')
    search_fields = ('name', 'room_number', 'teacher__name')


# Room Detail API View
class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Room
    serializer_class = serializers.RoomSerializer


# Room Update API View
class RoomUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Region Delete API View
class RoomDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]
