from django.db import models
from django.conf import settings

# https://hoik92.github.io/django/2019/06/11/Make-Profile-Page-Using-Django.html

# Create your models here.
# 프로필 모델 생성

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User 모델과 Pfofile을 1:1로 연결
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40,blank=True)
    # ImageField를 사용하기 위해 python pip install Pillow 패키지 설치 필요
    image = models.ImageField(blank=True)
