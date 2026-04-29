import uuid

from django.db import models

# Create your models here.

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубкрика'
        ordering = ['name']

class Bd(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубкрика')
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Содержание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    is_active = models.BooleanField(default=True, verbose_name='Активное', help_text='Активно ли объявление на сайте')

    # KIND = ((None, "Выбкрите тип публикуемого объявления"),
    #         ('b', "Куплю"),
    #         ('s', "Продам"),
    #         ('c', "Обменяю"))

    class Kind(models.TextChoices):
        BUY = 'b', "Куплю"
        SELL = 's', "Продам"
        EXCHANGE = 'c', "Обменяю"
        RENT = 'r', "Сдам"
        __empty__ = 'Выбкрите тип публикуемого объявления'

    kind = models.CharField(max_length=1, choices=Kind.choices, default=Kind.SELL, verbose_name='Тип объявления')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объяаление'
        ordering = ['-published', 'title']
        unique_together = ('published', 'title')
        # get_latest_by = '-published'
        # indexes = [models.Index(fields=['published', 'title'])]
