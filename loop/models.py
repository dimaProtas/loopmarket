from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='В наличии')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    new_models = models.BooleanField(default=False, null=True, verbose_name='Новинка')
    image = models.ImageField(upload_to='image/%y/%m/%d', blank=True, verbose_name='Изображение')
    quality = models.IntegerField(blank=True, verbose_name='Количество')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category', verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-price']


class User(models.Model):
    new_user = models.BooleanField(default=True, verbose_name='Подписка')
    email = models.EmailField(max_length=254, verbose_name='Почта', unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
