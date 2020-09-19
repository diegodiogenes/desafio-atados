from django.db import models
from users.models import User


# Create your models here.
class Action(models.Model):
    """
    Actions Model
    """
    # foreign keys
    volunteer = models.ManyToManyField(User, related_name='volunteers', help_text='Voluntários')
    # field
    name = models.TextField("Nome da Ação", help_text="Informe o nome da Ação")
    institute = models.TextField("Instituição", help_text="Instituição organizadora da ação")
    address = models.TextField("Local da Ação", help_text="Local da ação (cidade, bairro e endereço)")
    description = models.TextField("Descrição da Ação", help_text="Conte um pouco de como será a ação")