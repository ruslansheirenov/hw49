from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата Редактирования')

    class Meta:
        abstract = True

class TypeModel(models.Model):
    TYPE_CHOICES = [('Task', 'Задача'), ('Bug', 'Ошибка'), ('Enhancement', 'Улучшение')]
    types = models.CharField(max_length=11, choices=TYPE_CHOICES, default='Task', verbose_name='Тип')

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class StatusModel(models.Model):
    STATUS_CHOICES = [('New', 'Новая'), ('In Progress', 'В Процессе'), ('Done', 'Сделано')]
    statuses = models.CharField(max_length=11, choices=STATUS_CHOICES, default='New', verbose_name='Статус')

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Issue(BaseModel):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    status = models.ForeignKey('webapp.StatusModel', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('webapp.TypeModel', related_name='type', on_delete=models.PROTECT, verbose_name='Тип')

    class Meta:
        db_table = 'issues'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'