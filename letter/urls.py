from django.urls import path

from . import views


urlpatterns = [
    # Contact
    path('contacts/create/', views.ContactCreateAPIView.as_view()),
    path('contacts/', views.ContactListAPIView.as_view()),
    path('contacts/<int:pk>/', views.ContactDetailAPIView.as_view()),
    path('contacts/<int:pk>/update/', views.ContactUpdateAPIView.as_view()),
    path('contacts/<int:pk>/delete/', views.ContactDeleteAPIView.as_view()),

    # ContactType
    path('contact_types/create/', views.ContactTypeCreateAPIView.as_view()),
    path('contact_types/', views.ContactTypeListAPIView.as_view()),
    path('contact_types/<int:pk>/', views.ContactTypeDetailAPIView.as_view()),
    path('contact_types/<int:pk>/update/',
         views.ContactTypeUpdateAPIView.as_view()),
    path('contact_types/<int:pk>/delete/',
         views.ContactTypeDeleteAPIView.as_view()),

    # Message
    path('messages/create/', views.MessageCreateAPIView.as_view()),
    path('messages/', views.MessageListAPIView.as_view()),
    path('messages/<int:pk>/', views.MessageDetailAPIView.as_view()),
    path('messages/<int:pk>/update/', views.MessageUpdateAPIView.as_view()),
    path('messages/<int:pk>/delete/', views.MessageDeleteAPIView.as_view())
]
