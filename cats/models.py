from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cats(models.Model):
    name_c = models.CharField(max_length=20, verbose_name='Имя')
    age_c = models.CharField(max_length=20, verbose_name='Возраст')
    breed_c = models.CharField(max_length=20, verbose_name='Порода')
    type_of_wool_c = models.CharField(max_length=20, verbose_name='тип шерсти')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return str(self.name_c)

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описание"