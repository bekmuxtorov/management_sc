from django.urls import path
from . import views


urlpatterns = [
    # Season
    path('seasons/create/', views.SeasonCreateAPIView.as_view()),
    path('seasons/', views.SeasonListAPIView.as_view()),
    path('seasons/<int:pk>/', views.SeasonDetailAPIView.as_view()),
    path('seasons/<int:pk>/update/', views.SeasonUpdateAPIView.as_view()),
    path('seasons/<int:pk>/delete/', views.SeasonDeleteAPIView.as_view()),

    # PaymetType
    path('paymetTypes/create/', views.PaymetTypeCreateAPIView.as_view()),
    path('paymetTypes/', views.PaymetTypeListAPIView.as_view()),
    path('paymetTypes/<int:pk>/', views.PaymetTypeDetailAPIView.as_view()),
    path('paymetTypes/<int:pk>/update/',
         views.PaymetTypeUpdateAPIView.as_view()),
    path('paymetTypes/<int:pk>/delete/',
         views.PaymetTypeDeleteAPIView.as_view()),

    # Discount
    path('discounts/create/', views.DiscountCreateAPIView.as_view()),
    path('discounts/', views.DiscountListAPIView.as_view()),
    path('discounts/<int:pk>/', views.DiscountDetailAPIView.as_view()),
    path('discounts/<int:pk>/update/', views.DiscountUpdateAPIView.as_view()),
    path('discounts/<int:pk>/delete/', views.DiscountDeleteAPIView.as_view()),

    # Billing
    path('billings/create/', views.BillingCreateAPIView.as_view()),
    path('billings/', views.BillingListAPIView.as_view()),
    path('billings/<int:pk>/', views.BillingDetailAPIView.as_view()),
    path('billings/<int:pk>/update/', views.BillingUpdateAPIView.as_view()),
    path('billings/<int:pk>/delete/', views.BillingDeleteAPIView.as_view())
]
