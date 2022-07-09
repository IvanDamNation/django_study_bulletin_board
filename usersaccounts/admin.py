from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from usersaccounts.forms import UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    add_form = UserCreationForm
    list_display = ('id', 'username', 'email', 'is_activated', 'is_staff')
    list_editable = ('is_activated', )
