# Importações
from django.contrib import admin
from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    # Endpoint para uso da interface de administrador
    path('admin/', admin.site.urls),

    # Endpoint para obter o access token e o refresh token, deve ser enviado as informações de login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Endpoint para renovar o access point apartir do refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoint para registrar um novo usuário
    path('api/register/', views.register_user, name='register_user'),
    
    # Endpoint de teste do access token
    path('api/hello/', views.example_view, name='example_view'),

    # Endpoint para excluir os tokens e o armazenamento nos cookies
    path('api/logout', views.logout_view, name='logout')
]
