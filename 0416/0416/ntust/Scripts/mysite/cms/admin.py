from django.contrib import admin

# Register your models here.
from .models import Profile, ProfileIntro

admin.site.register(Profile)
admin.site.register(ProfileIntro) #註冊class讓它顯示在admin後台上


#python manage.py createsuperuser 用來創建管理員