from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата Редактирования')

    class Meta:
        abstract = True

class TypeModel(models.Model):
    types = models.CharField(max_length=11, verbose_name='Тип')

    def __str__(self):
        return self.types
    
    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class StatusModel(models.Model):
    statuses = models.CharField(max_length=11, verbose_name='Статус')

    def __str__(self):
        return self.statuses

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Issue(BaseModel):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    status = models.ForeignKey('webapp.StatusModel', related_name='tasks', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ManyToManyField('webapp.TypeModel', related_name='issues')

    class Meta:
        db_table = 'issues'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'