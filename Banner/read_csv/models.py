from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Banner(models.Model):

    url = models.CharField(max_length=200)
    shows = models.IntegerField(verbose_name="Кол-во показов")
    category = models.ManyToManyField(Category)
    # Это поле хранит дату когда был создан объект.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    # В этом поле хранится время последнего обновления объекта
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        ordering = ('shows',)  # сортировка
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.url
