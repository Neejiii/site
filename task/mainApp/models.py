from django.db import models


class Task(models.Model):
    title = models.CharField('Имя', max_length=60)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
