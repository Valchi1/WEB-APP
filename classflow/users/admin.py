from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Since no additional fields are added, you might not need to customize UserAdmin significantly
admin.site.register(CustomUser, UserAdmin)
