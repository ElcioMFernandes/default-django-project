# Importações
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	# Adicione campos adicionais aqui
      
    # Função que retorna o username do usuário quando chamado o modelo
    def __str__(self) -> str:
        return str(self.username)