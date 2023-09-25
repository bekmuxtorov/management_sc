from rest_framework import generics

from account import permissions as user_perm

from . import serializers
from . import models


# Contact


# Contact Create API View
class ContactCreateAPIView(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Contact List API View
class ContactListAPIView(generics.ListAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


# Contact Detail API View
class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


# Contact Update API View
class ContactUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Contact Delete API View
class ContactDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# ContactType


# ContactType Create API View
class ContactTypeCreateAPIView(generics.CreateAPIView):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# ContactType List API View
class ContactTypeListAPIView(generics.ListAPIView):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer


# ContactType Detail API View
class ContactTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer


# ContactType Update API View
class ContactTypeUpdateAPIView(generics.UpdateAPIView):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# ContactType Delete API View
class ContactTypeDeleteAPIView(generics.DestroyAPIView):
    queryset = models.ContactType.objects.all()
    serializer_class = serializers.ContactTypeSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Message


# Message Create API View
class MessageCreateAPIView(generics.CreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Message List API View
class MessageListAPIView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


# Message Detail API View
class MessageDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


# Message Update API View
class MessageUpdateAPIView(generics.UpdateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]


# Message Delete API View
class MessageDeleteAPIView(generics.DestroyAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [user_perm.IsDirectorOrAdminstrator]
