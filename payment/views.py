from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from account import permissions as user_perm

from . import models
from . import serializers


# Billing
class BillingCreateAPIView(generics.CreateAPIView):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.BillingSerializer


# Billing List API View
class BillingListAPIView(generics.ListAPIView):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.BillingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('study_center__name', 'study_group',
                        'payment_type', 'is_billing', 'payment_date', 'create_at')
    search_fields = ('student__user__full_name')


# Billing Detail API View
class BillingDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.BillingSerializer


# Billing Update API View
class BillingUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.BillingSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Billing Delete API View
class BillingDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.BillingSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Season
class SeasonCreateAPIView(generics.CreateAPIView):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer


# Season List API View
class SeasonListAPIView(generics.ListAPIView):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer
    filter_backends = [SearchFilter]
    search_fields = ('name',)


# Season Detail API View
class SeasonDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer


class SeasonUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


class SeasonDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# PaymetType
class PaymetTypeCreateAPIView(generics.CreateAPIView):
    queryset = models.PaymetType.objects.all()
    serializer_class = serializers.PaymetTypeSerializer


# PaymetType List API View
class PaymetTypeListAPIView(generics.ListAPIView):
    queryset = models.PaymetType.objects.all()
    serializer_class = serializers.PaymetTypeSerializer
    filter_backends = [SearchFilter]
    search_fields = ('name',)


class PaymetTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.PaymetType.objects.all()
    serializer_class = serializers.PaymetTypeSerializer


class PaymetTypeUpdateAPIView(generics.UpdateAPIView):
    queryset = models.PaymetType.objects.all()
    serializer_class = serializers.PaymetTypeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


class PaymetTypeDeleteAPIView(generics.DestroyAPIView):
    queryset = models.PaymetType.objects.all()
    serializer_class = serializers.PaymetTypeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Discount
class DiscountCreateAPIView(generics.CreateAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer


# Discount List API View
class DiscountListAPIView(generics.ListAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ('study_center', 'type',
                        'start_date', 'end_date', 'status')
    search_fields = ('name', 'start_date', 'end_date')


class DiscountDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer


class DiscountUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


class DiscountDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]
