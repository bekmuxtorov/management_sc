import json
from rest_framework import serializers
from study_center.serializers import StudyCenterNameSerializer, SubjectNameSerializer
from study_center.models import StudyCenter, Subject
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
        fields = ('id', 'phone_number', 'full_name', 'study_center', 'is_phone_verified',
                  'passport_or_id', 'passport_or_id_number', 'study_center', 'password', 'password2')

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        phone_number = validated_data.get('phone_number')
        full_name = validated_data.get('full_name')
        study_center = validated_data.get('study_center')
        passport_or_id = validated_data.get('passport_or_id')
        passport_or_id_number = validated_data.get('passport_or_id_number')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            adminstrator_user = models.User(
                type='adminstrator',
                phone_number=phone_number,
                full_name=full_name,
                study_center=study_center,
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


class TeacherRegisterSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    salary_percentage = serializers.FloatField()
    phone_number = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)
    subject = serializers.CharField()
    study_center = serializers.CharField()
    passport_or_id = serializers.CharField()
    passport_or_id_number = serializers.CharField()

    def create(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.pop('password2')
        study_center_id = validated_data.pop('study_center')
        subject_id = validated_data.pop('subject')

        study_center = StudyCenter.objects.filter(id=study_center_id).first()
        subject = Subject.objects.filter(id=subject_id).first()

        if password == password2:
            user = models.User(
                type='teacher',
                study_center=study_center,
                subject=subject,
                **validated_data
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Both passwords do not match'
            })

    def update(self, instance, validated_data):
        print(''.join(['<', '='*10, '>', 'asdasdf']))
        return super().update(instance, validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('password', 'last_login', 'is_superuser',
                   'groups', 'user_permissions', 'is_staff')


class TeacherSerializer(serializers.ModelSerializer):
    study_center = StudyCenterNameSerializer()
    subject = SubjectNameSerializer()

    class Meta:
        model = models.User
        fields = ('id', 'phone_number', 'full_name', 'is_phone_verified', 'study_center',
                  'passport_or_id', 'passport_or_id_number', 'subject', 'salary_percentage')

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }


class StudentRegisterSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    phone_number = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)
    subject = serializers.CharField(required=True)
    study_center = serializers.CharField(required=True)
    passport_or_id = serializers.CharField(required=True)
    passport_or_id_number = serializers.CharField(required=True)

    def create(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.pop('password2')
        study_center_id = validated_data.pop('study_center')
        subject_id = validated_data.pop('subject')

        study_center = StudyCenter.objects.filter(id=study_center_id).first()
        subject = Subject.objects.filter(id=subject_id).first()

        if password == password2:
            user = models.User(
                type='student',
                study_center=study_center,
                subject=subject,
                **validated_data
            )
            user.set_password(password)
            user.save()

            return user


class StudentSerializer(serializers.ModelSerializer):
    study_center = StudyCenterNameSerializer()
    subject = SubjectNameSerializer()

    class Meta:
        model = models.User
        fields = ('id', 'phone_number', 'full_name', 'is_phone_verified', 'subject',  'study_center',
                  'passport_or_id', 'passport_or_id_number')
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
