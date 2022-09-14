from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone


# Create your models here.
class CountryItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    name_country = models.CharField(max_length=50, verbose_name='Название страны', unique=True)

    def get_absolute_url(self):
        return f'/api/countries'

    def __str__(self):
        return f'Страна: {self.name_country}'


class ProducerItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    name_producer = models.CharField(max_length=50, verbose_name='Название производителя', unique=True)
    name_country = models.ForeignKey(CountryItem, verbose_name='Название страны', related_name='producers',
                                     on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/api/producers'

    def __str__(self):
        return f'Производитель: {self.name_producer}'


class CarItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    name_car = models.CharField(max_length=50, verbose_name='Название машины', unique=True)
    name_producer = models.ForeignKey(ProducerItem, verbose_name='Имя производителя', related_name='cars',
                                      on_delete=models.CASCADE)
    year_start = models.DateField(verbose_name='Год начала выпуска')
    year_end = models.DateField(verbose_name='Год окончания выпуска')

    def get_absolute_url(self):
        return f'/api/cars'

    def __str__(self):
        return f'Название машины: {self.name_car}'


class CommentItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Комменатрий '
        verbose_name_plural = 'Комментарии'

    email_name = models.EmailField(max_length=50, verbose_name='Электронная почта автора:',
                                   validators=[EmailValidator(
                                       message='Введите конкретный email'
                                   )])
    name_car = models.ForeignKey(CarItem, verbose_name='Название машины', related_name='comments',
                                 on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='Дата создания поста', default=timezone.now)
    comment = models.CharField(max_length=250, verbose_name='Комментарий:')

    def get_absolute_url(self):
        return f'/api/comments'

    def __str__(self):
        return f'Комментарий: {self.comment}'
