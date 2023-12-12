from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]
        error_messages = {
            "email": {"unique": "Email is Already Exists."},
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]
