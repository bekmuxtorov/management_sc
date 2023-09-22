from django.urls import path

from . import views


urlpatterns = [
    # Subject
    ('subjects/', views.SubjectListAPIView.as_view()),
    ('subjects/create/', views.SubjectCreateAPIVIew.as_view()),
    ('subjects/<int:pk>/', views.SubjectDetailAPIView.as_view()),
    ('subjects/<int:pk>/update/', views.SubjectUpdateAPIView.as_view()),
    ('subjects/<int:pk>/delete/', views.SubjectDeleteAPIView.as_view()),

    # StudyCenter
    ('studycenters/', views.StudyCenterListAPIView.as_view()),
    ('studycenters/create/', views.StudyCenterCreateAPIVIew.as_view()),
    ('studycenters/<int:pk>/', views.StudyCenterDetailAPIView.as_view()),
    ('studycenters/<int:pk>/update/', views.StudyCenterUpdateAPIView.as_view()),
    ('studycenters/<int:pk>/delete/', views.StudyCenterDeleteAPIView.as_view()),


    # SubjectGroup
    ('subject_groups/', views.SubjectGroupListAPIView.as_view()),
    ('subject_groups/create/', views.SubjectGroupCreateAPIVIew.as_view()),
    ('subject_groups/<int:pk>/', views.SubjectGroupDetailAPIView.as_view()),
    ('subject_groups/<int:pk>/update/', views.SubjectGroupUpdateAPIView.as_view()),
    ('subject_groups/<int:pk>/delete/', views.SubjectGroupDeleteAPIView.as_view()),

    # StudyDay
    ('study_days/', views.StudyDayListAPIView.as_view()),
    ('study_days/create/', views.StudyDayCreateAPIVIew.as_view()),
    ('study_days/<int:pk>/', views.StudyDayDetailAPIView.as_view()),
    ('study_days/<int:pk>/update/', views.StudyDayUpdateAPIView.as_view()),
    ('study_days/<int:pk>/delete/', views.StudyDayDeleteAPIView.as_view()),

    # Time
    ('times/', views.TimeListAPIView.as_view()),
    ('times/create/', views.TimeCreateAPIVIew.as_view()),
    ('times/<int:pk>/', views.TimeDetailAPIView.as_view()),
    ('times/<int:pk>/update/', views.TimeUpdateAPIView.as_view()),
    ('times/<int:pk>/delete/', views.TimeDeleteAPIView.as_view()),

    # Day
    ('days/', views.DayListAPIView.as_view()),
    ('days/create/', views.DayCreateAPIVIew.as_view()),
    ('days/<int:pk>/', views.DayDetailAPIView.as_view()),
    ('days/<int:pk>/update/', views.DayUpdateAPIView.as_view()),
    ('days/<int:pk>/delete/', views.DayDeleteAPIView.as_view()),

    # Room
    ('rooms/', views.RoomListAPIView.as_view()),
    ('rooms/create/', views.RoomCreateAPIVIew.as_view()),
    ('rooms/<int:pk>/', views.RoomDetailAPIView.as_view()),
    ('rooms/<int:pk>/update/', views.RoomUpdateAPIView.as_view()),
    ('rooms/<int:pk>/delete/', views.RoomDeleteAPIView.as_view()),

]
