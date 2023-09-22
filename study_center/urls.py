from django.urls import path

from . import views


urlpatterns = [
    # Subject
    path('subjects/', views.SubjectListAPIView.as_view()),
    path('subjects/create/', views.SubjectCreateAPIVIew.as_view()),
    path('subjects/<int:pk>/', views.SubjectDetailAPIView.as_view()),
    path('subjects/<int:pk>/update/', views.SubjectUpdateAPIView.as_view()),
    path('subjects/<int:pk>/delete/', views.SubjectDeleteAPIView.as_view()),

    # StudyCenter
    path('studycenters/', views.StudyCenterListAPIView.as_view()),
    path('studycenters/create/', views.StudyCenterCreateAPIVIew.as_view()),
    path('studycenters/<int:pk>/', views.StudyCenterDetailAPIView.as_view()),
    path('studycenters/<int:pk>/update/', views.StudyCenterUpdateAPIView.as_view()),
    path('studycenters/<int:pk>/delete/', views.StudyCenterDeleteAPIView.as_view()),


    # SubjectGroup
    path('subject_groups/', views.SubjectGroupListAPIView.as_view()),
    path('subject_groups/create/', views.SubjectGroupCreateAPIVIew.as_view()),
    path('subject_groups/<int:pk>/', views.SubjectGroupDetailAPIView.as_view()),
    path('subject_groups/<int:pk>/update/', views.SubjectGroupUpdateAPIView.as_view()),
    path('subject_groups/<int:pk>/delete/', views.SubjectGroupDeleteAPIView.as_view()),

    # StudyDay
    path('study_days/', views.StudyDayListAPIView.as_view()),
    path('study_days/create/', views.StudyDayCreateAPIVIew.as_view()),
    path('study_days/<int:pk>/', views.StudyDayDetailAPIView.as_view()),
    path('study_days/<int:pk>/update/', views.StudyDayUpdateAPIView.as_view()),
    path('study_days/<int:pk>/delete/', views.StudyDayDeleteAPIView.as_view()),

    # Time
    path('times/', views.TimeListAPIView.as_view()),
    path('times/create/', views.TimeCreateAPIVIew.as_view()),
    path('times/<int:pk>/', views.TimeDetailAPIView.as_view()),
    path('times/<int:pk>/update/', views.TimeUpdateAPIView.as_view()),
    path('times/<int:pk>/delete/', views.TimeDeleteAPIView.as_view()),

    # Day
    path('days/', views.DayListAPIView.as_view()),
    path('days/create/', views.DayCreateAPIVIew.as_view()),
    path('days/<int:pk>/', views.DayDetailAPIView.as_view()),
    path('days/<int:pk>/update/', views.DayUpdateAPIView.as_view()),
    path('days/<int:pk>/delete/', views.DayDeleteAPIView.as_view()),

    # Room
    path('rooms/', views.RoomListAPIView.as_view()),
    path('rooms/create/', views.RoomCreateAPIVIew.as_view()),
    path('rooms/<int:pk>/', views.RoomDetailAPIView.as_view()),
    path('rooms/<int:pk>/update/', views.RoomUpdateAPIView.as_view()),
    path('rooms/<int:pk>/delete/', views.RoomDeleteAPIView.as_view()),

]
