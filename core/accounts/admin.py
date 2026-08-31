from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_active', 'is_superuser')    
    list_filter = ('email', 'is_active', 'is_superuser')
    searching_fields = ['email']
    ordering = ['email']
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),
        ('permissions', {
            "fields": (
                'is_staff', 'is_active', 'is_superuser'
            ),
        }),
        ('group_permissions'
            , {
                'fields': (
                    'groups', 'user_permissions'
                ),
            }   
        ),
        ('Important dates', {
            'fields': (
                'last_login', 'date_joined'
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2' ,'is_staff', 'is_active', 'is_superuser'),
        }), 
    )
admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)