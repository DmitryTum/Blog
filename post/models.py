from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    class Meta():
        db_table = 'post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['create']

    title = models.CharField('Заголоваок', max_length=100)
    text = models.TextField('Текст статьи', max_length=1200)
    image = models.ImageField('Изображение', upload_to='post/', blank=True)
    create = models.DateTimeField('Создание', auto_now_add=True)
    update = models.DateTimeField('Обновление', auto_now=True)
    moder = models.BooleanField('Модерация', default=False)

    def __str__(self):
        return self.title


class CommentPost(models.Model):
    class Meta():
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    text = models.TextField('Текст коммента')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Дата коммента')
    moder = models.BooleanField(default=False)
