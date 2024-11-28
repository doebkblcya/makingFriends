from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'birthday', 'phone_number', 'region', 'tier')
    list_filter = ('is_staff', 'is_active', 'region', 'tier')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'birthday', 'phone_number', 'profile_picture')}),
        ('Region & Tier', {'fields': ('region', 'tier')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'birthday', 'phone_number', 'region', 'tier')}
        ),
    )

# 注册自定义用户模型和管理类
admin.site.register(CustomUser, CustomUserAdmin)
