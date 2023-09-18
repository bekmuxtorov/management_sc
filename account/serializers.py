from rest_framework import serializers
from study_center.serializers import SubjectSerializer

from . import models


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=True)

    class Meta:
        model = models.District
        fields = '__all__'


class DirectorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.User
        fields = ('phone_number', 'full_name',
                  'passport_or_id', 'passport_or_id_number', 'password', 'password2')

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        full_name = validated_data.get('full_name')
        passport_or_id = validated_data.get('passport_or_id')
        passport_or_id_number = validated_data.get('passport_or_id_number')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            director_user = models.User(
                type='director',
                phone_number=phone_number,
                full_name=full_name,
                passport_or_id=passport_or_id,
                passport_or_id_number=passport_or_id_number
            )
            director_user.set_password(password)
            director_user.save()
            return director_user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })


class AdminstratorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = models.User
        fields = ('phone_number', 'full_name',
                  'passport_or_id', 'passport_or_id_number', 'password', 'password2')

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        full_name = validated_data.get('full_name')
        passport_or_id = validated_data.get('passport_or_id')
        passport_or_id_number = validated_data.get('passport_or_id_number')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            adminstrator_user = models.User(
                type='adminstrator',
                phone_number=phone_number,
                full_name=full_name,
                passport_or_id=passport_or_id,
                passport_or_id_number=passport_or_id_number
            )
            adminstrator_user.set_password(password)
            adminstrator_user.save()
            return adminstrator_user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })


class TeacherRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    phone_number = serializers.CharField(required=True)
    full_name = serializers.CharField()
    passport_or_id = serializers.CharField()
    passport_or_id_number = serializers.CharField()

    class Meta:
        model = models.TeacherUser
        fields = ('phone_number', 'full_name',
                  'passport_or_id', 'passport_or_id_number', 'subject', 'salary_percentage', 'password', 'password2')

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        full_name = validated_data.get('full_name')
        passport_or_id = validated_data.get('passport_or_id')
        passport_or_id_number = validated_data.get('passport_or_id_number')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        subject = validated_data.get('subject')
        salary_percentage = validated_data.get('salary_percentage')

        if password == password2:
            user = models.User(
                type='teacher',
                phone_number=phone_number,
                full_name=full_name,
                passport_or_id=passport_or_id,
                passport_or_id_number=passport_or_id_number
            )
            user.set_password(password)
            user.save()

            teacher_user = models.TeacherUser(
                user=user,
                subject=subject,
                salary_percentage=salary_percentage
            )
            teacher_user.save()
            return teacher_user, user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })
