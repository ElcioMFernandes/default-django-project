# Importações
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Define o User como o usuário que está definido em AUTH_USER_MODEL no settings.py
User = get_user_model()

# Serializador do usuário
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password', 'email')
		extra_kwargs = {'password': {'write_only': True}}

	# Função que cria o usuário em caso de validação dos campos informados
	def create(self, validated_data):
		user = User.objects.create_user(
			username=validated_data['username'],
			email=validated_data['email'],
			password=validated_data['password']
		)
		return user