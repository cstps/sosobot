from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from django.contrib.auth.forms import UserChangeForm
from .models import Profile

# 회원가입 폼 상속 받아 확장
class CreateUserForm(UserCreationForm): 
    username = forms.CharField(
        label="ID",
        widget=forms.TextInput(attrs={
            "placeholder": "사용자 아이디",
        })
    )
    password1 = forms.CharField(
        label="PASSWORD",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 입력(8자 이상)",
        })
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호 확인",
        })
    )

    class Meta:
        model = User
        fields = ("username",  "password1", "password2")

