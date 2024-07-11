# Importações
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . import serializers

# Exemplo
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request):
	content = {'message': 'Hello, World!'}
	return Response(content)

# Registrar usuário
@api_view(['POST'])
def register_user(request):
	serializer = serializers.UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({"message": "User created successfully"}, status=201)
	else:
		return Response({"message": "User not created"}, status=400)

# Recuperar Token de refresh e access
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Faz login com as credenciais do usuário e retorna os tokens
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        tokens = get_tokens_for_user(user)
        response = JsonResponse({'message': 'Login bem-sucedido'})
        response.set_cookie(
            'access_token',
            tokens['access'],
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        return response
    else:
        return Response({"message": "Credenciais inválidas"}, status=401)

# Faz logoff do usuário
def logout_view(request):
    response = JsonResponse({'message': 'Logout bem-sucedido'})
    response.delete_cookie('access_token')
    return response