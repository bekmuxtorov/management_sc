from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from . import models
from . import serializers


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            required=['phone_number', 'password'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="User login",
                examples={
                    'application/json': {
                        "id": 20,
                        "type": "director",
                        "phone_number": "+998907778183",
                        "full_name": "Palonchiyev Pistonchi",
                        "passport_or_id": "passport",
                        "passport_or_id_number": "asdf",
                        "is_phone_verified": False,
                        "created_at": "2023-09-17T08:30:03.431503Z",
                        "token": "Token ec5dddc88e4",
                        "study_center": None
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        'error': 'Both passwords do not match'
                    }
                }
            )
        }
    )
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = authenticate(
            phone_number=phone_number,
            password=password
        )
        if user:
            user_data = {
                'id': user.id,
                'type': user.type,
                'phone_number': user.phone_number,
                'full_name': user.full_name,
                'passport_or_id': user.passport_or_id,
                'passport_or_id_number': user.passport_or_id_number,
                'is_phone_verified': user.is_phone_verified,
                'created_at': user.created_at,
                'token': f"Token {Token.objects.get_or_create(user=user)[0].key}"
            }

            if user.type == 'teacher':
                user_data.update({
                    'subject': user.teacher_user.subject.name,
                    'salary_percentage': user.teacher_user.salary_percentage
                })

            elif user.type == 'student':
                user_data['subject'] = user.student_user.subject.name

            try:
                user_data['study_center'] = user.study_center.name
            except:
                user_data['study_center'] = None

            return Response(user_data, status=status.HTTP_200_OK)
        return Response({'error': 'There is an error in the login or password'}, status=status.HTTP_404_NOT_FOUND)


class DirectorRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.DirectorRegisterSerializer

    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            required=['phone_number', 'password'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description='Full Name'),
                "passport_or_id": openapi.Schema(type=openapi.TYPE_STRING, enum=['passport', 'document_id'], description='Passport or ID'),
                "passport_or_id_number": openapi.Schema(type=openapi.TYPE_STRING, description="Password or id number"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password2'),
            }
        ),
        responses={
            200: openapi.Response(
                description="User login",
                examples={
                    'application/json': {
                        "token": "Token cd055696",
                        "type": "director",
                        "phone_number": "+998907778111",
                        "full_name": "Palonchiyev Pistonchi",
                        "passport_or_id": "passport",
                        "passport_or_id_number": "asdf",
                        "is_phone_number": False,
                        "created_at": "2023-09-17T08:44:15.663502Z"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        'error': 'Invalid credentials'
                    }
                }
            )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            request_data = {
                'token': f"Token {token}",
                'type': user.type,
                'phone_number': user.phone_number,
                'full_name': user.full_name,
                'passport_or_id': user.passport_or_id,
                'passport_or_id_number': user.passport_or_id_number,
                'is_phone_number': user.is_phone_verified,
                'created_at': user.created_at
            }
            return Response(request_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminstratorRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.AdminstratorRegisterSerializer

    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            required=['phone_number', 'password'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description='Full Name'),
                "passport_or_id": openapi.Schema(type=openapi.TYPE_STRING, enum=['passport', 'document_id'], description='Passport or ID'),
                "passport_or_id_number": openapi.Schema(type=openapi.TYPE_STRING, description="Password or id number"),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password2'),
            }
        ),
        responses={
            200: openapi.Response(
                description="User login",
                examples={
                    'application/json': {
                        "token": "Toekn cd055696",
                        "type": "adminstrator",
                        "phone_number": "+998907778111",
                        "full_name": "Palonchiyev Pistonchi",
                        "passport_or_id": "passport",
                        "passport_or_id_number": "asdf",
                        "is_phone_number": False,
                        "created_at": "2023-09-17T08:44:15.663502Z"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        'error': 'Invalid credentials'
                    }
                }
            )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            request_data = {
                'token': f"Token {token}",
                'type': user.type,
                'phone_number': user.phone_number,
                'full_name': user.full_name,
                'passport_or_id': user.passport_or_id,
                'passport_or_id_number': user.passport_or_id_number,
                'is_phone_number': user.is_phone_verified,
                'created_at': user.created_at
            }
            return Response(request_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.TeacherRegisterSerializer

    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            required=['phone_number', 'password'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description='Full Name'),
                "passport_or_id": openapi.Schema(type=openapi.TYPE_STRING, enum=['passport', 'document_id'], description='Passport or ID'),
                "passport_or_id_number": openapi.Schema(type=openapi.TYPE_STRING, description="Password or id number"),
                "subject": openapi.Schema(type=openapi.TYPE_INTEGER, description='The id field of the object of the Subject model'),
                'salary_percentage': openapi.Schema(type=openapi.TYPE_STRING, description='Salary percentage'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password2'),
            }
        ),
        responses={
            201: openapi.Response(
                description="User login",
                examples={
                    'application/json': {
                        "token": "Token 1cd055696",
                        "type": "teacher",
                        "phone_number": "+998907778111",
                        "full_name": "Palonchiyev Pistonchi",
                        "passport_or_id": "passport",
                        "passport_or_id_number": "asdf",
                        "is_phone_number": False,
                        'subject': {
                            'id': 1,
                            'name': 'Physics'
                        },
                        'salary_percentage': '40.0',
                        "created_at": "2023-09-17T08:44:15.663502Z"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        'error': 'Registered user'
                    }
                }
            )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            if models.User.objects.filter(phone_number=phone_number).exists():
                return Response(data={'error': 'Registered user'}, status=status.HTTP_400_BAD_REQUEST)

            teacher_user, user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            request_data = {
                'token': f"Token {token}",
                'type': user.type,
                'phone_number': user.phone_number,
                'full_name': user.full_name,
                'passport_or_id': user.passport_or_id,
                'passport_or_id_number': user.passport_or_id_number,
                'is_phone_number': user.is_phone_verified,
                'created_at': user.created_at,
                'subject': {
                    'id': teacher_user.subject.id,
                    'name': teacher_user.subject.name
                },
                'salary_percentage': teacher_user.salary_percentage
            }
            return Response(request_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentRegisterAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.StudentRegisterSerializer

    @swagger_auto_schema(
        operation_description="Login user",
        request_body=openapi.Schema(
            required=['phone_number', 'password'],
            type=openapi.TYPE_OBJECT,
            properties={
                'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number'),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description='Full Name'),
                "passport_or_id": openapi.Schema(type=openapi.TYPE_STRING, enum=['passport', 'document_id'], description='Passport or ID'),
                "passport_or_id_number": openapi.Schema(type=openapi.TYPE_STRING, description="Password or id number"),
                "subject": openapi.Schema(type=openapi.TYPE_INTEGER, description='The id field of the object of the Subject model'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
                'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Password2'),
            }
        ),
        responses={
            201: openapi.Response(
                description="User login",
                examples={
                    'application/json': {
                        "token": "Token 2cbbb7a1d939",
                        "type": "student",
                        "phone_number": "+998907778111",
                        "full_name": "Palonchiyev Pistonchi",
                        "passport_or_id": "passport",
                        "passport_or_id_number": "asdf",
                        "is_phone_number": False,
                        'subject': {
                            'id': 1,
                            'name': 'Physics'
                        },
                        "created_at": "2023-09-17T08:44:15.663502Z"
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request",
                examples={
                    'application/json': {
                        'error': 'Registered user'
                    }
                }
            )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get('phone_number')
            if models.User.objects.filter(phone_number=phone_number).exists():
                return Response(data={'error': 'Registered user'}, status=status.HTTP_400_BAD_REQUEST)

            student_user, user = serializer.save()
            token = Token.objects.get_or_create(user=user)[0].key
            request_data = {
                'token': f"Token {token}",
                'type': user.type,
                'phone_number': user.phone_number,
                'full_name': user.full_name,
                'passport_or_id': user.passport_or_id,
                'passport_or_id_number': user.passport_or_id_number,
                'is_phone_number': user.is_phone_verified,
                'created_at': user.created_at,
                'subject': {
                    'id': student_user.subject.id,
                    'name': student_user.subject.name
                },
            }
            return Response(request_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
