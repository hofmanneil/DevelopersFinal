from django.db import models
from django.contrib.auth.models import AbstractUser


class MainUser(AbstractUser):
    teudat_zehut = models.CharField(max_length = 20 )
