from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User Model
    """
    # fields
    first_name = models.TextField("Nome", help_text="Informe o seu primeiro nome")
    last_name = models.TextField("Sobrenome", help_text="Informe o seu sobrenome")
    email = models.EmailField("Email", unique=True, help_text="Informe o email do voluntário")
    district = models.TextField("Bairro", help_text="Informe o Bairro do Voluntário")
    city = models.TextField("Cidade", help_text="Informe a Cidade do Voluntário")

    class Meta:
        ordering = ['id']
