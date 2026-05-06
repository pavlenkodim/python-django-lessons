from django.db import models
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
# import uuid
from django.core import validators

# custom validations
from bboard.utils.validators import get_min_length, validate_even, MinMaxValueValidator


# Create your models here.
class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/bboard/%s/" % self.pk

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубкрика'
        ordering = ['name']

class Bd(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Рубкрика')
    title = models.CharField(
        max_length=50,
        validators=[
            validators.RegexValidator(regex='^.{4}$'),
            validators.MinLengthValidator(get_min_length),
            validate_even],
            # MinMaxValueValidator(50, 100)],
        verbose_name='Название',
        error_messages={
            'invalid': "Неправильное название объявления",
            'unique': "Объявление с таким имененем уже существует",
            'odd': "Some error"})
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

    def title_and_price(self):
        if self.price:
            return "%s (%.2f)" % (self.title, self.price)
        else:
            return self.title

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('укажите чтонибудь')
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Цена не может быть отрицательной')

        # errors[NON_FIELD_ERRORS] = ValidationError('Ошибка с моделью')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title']
        unique_together = ('published', 'title')
        # get_latest_by = '-published'
        # indexes = [models.Index(fields=['published', 'title'])]
