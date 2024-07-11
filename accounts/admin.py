# Importações
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Registrando o modelo no Admin
admin.site.register(CustomUser, UserAdmin)
