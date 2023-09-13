from django.contrib.auth.forms import UserCreationForm as OldUserCreationForm, UserChangeForm as OldUserChangeForm

from .models import User


class UserCreationForm(OldUserCreationForm):
    class Meta:
        model = User
        fields = ("phone_number", "full_name")


class UserChangeForm(OldUserChangeForm):
    class Meta:
        model = User
        fields = ("phone_number", "type", "full_name", "study_center",
                  "password_or_id_number", "is_staff", "is_superuser")
