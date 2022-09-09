from django.db import models
from django.core.validators import EmailValidator


# Create your models here.
class CountryItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    name = models.CharField(max_length=50, verbose_name='Название страны', unique=True)

    def __str__(self):
        return f'Страна: {self.name}'


class ProducerItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    name = models.CharField(max_length=50, verbose_name='Название производителя', unique=True)
    country = models.ForeignKey(CountryItem, verbose_name='Название страны', related_name='countries',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'Производитель: {self.name}'


class CarItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    name = models.CharField(max_length=50, verbose_name='Название машины', unique=True)
    producer = models.ForeignKey(ProducerItem, verbose_name='Имя производителя', related_name='producers',
                                 on_delete=models.CASCADE)
    year_start = models.DateField(verbose_name='Год начала выпуска')
    year_end = models.DateField(verbose_name='Год окончания выпуска')

    class CarItem(models.Model):
        objects = models.Manager()

        class Meta:
            verbose_name = 'Машина'
            verbose_name_plural = 'Машины'

        name = models.CharField(max_length=50, verbose_name='Название новости', unique=True)
        producer = models.ForeignKey(ProducerItem, verbose_name='Имя производителя', related_name='producers',
                                     on_delete=models.CASCADE)
        year_start = models.DateField(verbose_name='Год начала выпуска')
        year_end = models.DateField(verbose_name='Год окончания выпуска')

    def __str__(self):
        return f'Название машины: {self.name}'


class CommentItem(models.Model):
    objects = models.Manager()

    class Meta:
        verbose_name = 'Комменатрий '
        verbose_name_plural = 'Комментарии'

    email_name = models.EmailField(max_length=50, verbose_name='Электронная почта автора:',
                                   validators=[EmailValidator(
                                       message='Введите конкретный email'
                                   )])
    car = models.ForeignKey(CarItem, verbose_name='Название машины', related_name='comments', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')
    comment = models.CharField(max_length=250, verbose_name='Комментарий:')

    def __str__(self):
        return f'Комментарий: {self.comment}'
