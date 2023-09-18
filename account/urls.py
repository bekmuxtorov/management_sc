from django.urls import path
from . import views


urlpatterns = [
    # Register
    path('auth/register/director/', views.DirectorRegisterAPIView.as_view()),
    path('auth/register/adminstrator/', views.AdminstratorRegisterAPIView.as_view()),
    path('auth/register/teacher/', views.TeacherRegisterAPIView.as_view()),
    path('auth/register/student/', views.StudentRegisterAPIView.as_view()),

    # Login
    path('auth/login/', views.UserLoginAPIView.as_view()),
]
