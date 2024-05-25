from django.db import models
import datetime

class Animal(models.Model):
    TYPE_CHOICES = (
        ('mammal', 'Млекопитающее'),
        ('fish', 'Рыба'),
        ('reptile', 'Рептилия'),
        ('birds', 'Пернатые'),
    )

    name = models.CharField('Название', max_length=100)
    type = models.CharField('Род', max_length=100, choices=TYPE_CHOICES, default='mammal')

    information = models.TextField('Информация', blank=True)
    population = models.PositiveIntegerField('Популяция', default=0)
    is_rare = models.BooleanField('Вымерающие животные', default=False)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self) -> str:
        return self.name
