from rest_framework import serializers

from . import models


# Billing
class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Billing
        fields = '__all__'


# Season
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Season
        fields = '__all__'


# PaymetType
class PaymetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymetType
        fields = '__all__'


# Discount
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discount
        fields = '__all__'
