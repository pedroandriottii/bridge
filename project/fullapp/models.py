from django.db import models
from django.contrib.auth.models import AbstractUser

class RegionEnum:
    ACRE = 'Acre'
    ALAGOAS = 'Alagoas'
    AMAPA = 'Amapá'
    AMAZONAS = 'Amazonas'
    BAHIA = 'Bahia'
    CEARA = 'Ceará'
    DISTRITO_FEDERAL = 'Distrito Federal'
    ESPIRITO_SANTO = 'Espírito Santo'
    GOIAS = 'Goiás'
    MARANHAO = 'Maranhão'
    MATO_GROSSO = 'Mato Grosso'
    MATO_GROSSO_DO_SUL = 'Mato Grosso do Sul'
    MINAS_GERAIS = 'Minas Gerais'
    PARA = 'Pará'
    PARAIBA = 'Paraíba'
    PARANA = 'Paraná'
    PERNAMBUCO = 'Pernambuco'
    PIAUI = 'Piauí'
    RIO_DE_JANEIRO = 'Rio de Janeiro'
    RIO_GRANDE_DO_NORTE = 'Rio Grande do Norte'
    RIO_GRANDE_DO_SUL = 'Rio Grande do Sul'
    RONDONIA = 'Rondônia'
    RORAIMA = 'Roraima'
    SANTA_CATARINA = 'Santa Catarina'
    SAO_PAULO = 'São Paulo'
    SERGIPE = 'Sergipe'
    TOCANTINS = 'Tocantins'

class StatusEnum:
    REJECTED = 'Rejected'
    LOOKING_FOR_DONORS = 'Looking for donors'
    IN_ANALISYS = 'In analisys'
    APPROVED = 'Approved'
    DONORS_FOUND = 'Donors found'
    EXITED = 'Exited'
    CONCLUDED = 'Concluded'
    DEACTIVATED = 'Deactivated'

def get_choices(constants_class: any) -> list[tuple[str, str]]:
    return [
        (value, value)
        for key, value in vars(constants_class).items()
        if not key.startswith('__')
    ]

class User(AbstractUser):
    ADMIN = 1
    AMBASSADOR = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (AMBASSADOR, 'Ambassador'),
        (USER, 'User'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=USER)

    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    project = models.CharField(max_length=50, null=True, blank=True)
    objective = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(choices=get_choices(RegionEnum), default=RegionEnum.PERNAMBUCO, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username

class Demand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(choices=get_choices(StatusEnum), default=StatusEnum.IN_ANALISYS, max_length=255, null=True, blank=True)
    region = models.CharField(choices=get_choices(RegionEnum), default=RegionEnum.PERNAMBUCO, max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title