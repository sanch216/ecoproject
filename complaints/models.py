from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено')
    ]

    THREAT_CHOICES = [
        ('low', 'Малая угроза'),
        ('high', 'Большая угроза')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    photo = models.ImageField(upload_to='complaints/', verbose_name="Фото мусора")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=255, verbose_name="Адрес")
    threat_level = models.CharField(max_length=10, choices=THREAT_CHOICES, verbose_name="Уровень угрозы")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.location} ({self.get_threat_level_display()})"


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Волонтёр")
    cleaned_count = models.IntegerField(default=0, verbose_name="Количество убранного мусора")

    def __str__(self):
        return self.user.username
