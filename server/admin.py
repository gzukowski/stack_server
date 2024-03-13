from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'wins', 'losses')


@admin.register(Task)
class Tasks(admin.ModelAdmin):
    list_display = ('task_id', 'correct_answer', 'is_completed')