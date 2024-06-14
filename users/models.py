from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="image_users", blank=True, null=True, verbose_name="Аватар")
    
    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
