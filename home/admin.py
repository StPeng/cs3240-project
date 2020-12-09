# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model

# /***************************************************************************************
# *  REFERENCES
# *  Title: How to Add User Profile To Django Admin
# *  Author: Vitor Freitas
# *  Date Accessed: 11/06/2020
# *  Date Published: 11/23/2016
# *  Code version: N/A
# *  URL: https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
# *  Software License: CC BY-NC-SA 3.0
# *
# *
# *  Title: Extending the Existing User Model
# *  Author: Django Software Foundation
# *  Date Accessed: 11/06/2020
# *  Code version: 3.1
# *  URL: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model
# *  Software License: BSD-3
# ***************************************************************************************/

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile
from .models import Issue

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Issue)
