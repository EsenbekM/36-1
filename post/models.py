'''
models.py - файл, который содержит описание базы данных.
'''

from django.db import models


class HashTag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Post(models.Model):
    photo = models.ImageField(upload_to="post_photos/%Y/%m/%d", null=True,
                              verbose_name="Фото") # ImageField - поле для загрузки изображения
    title = models.CharField(max_length=100, verbose_name="Название") # CharField - поле для ввода текста с ограничением по количеству символов
    content = models.TextField(null=True, blank=True) # TextField - поле для ввода текста без ограничения по количеству символов
    rate = models.FloatField(default=0) # FloatField - поле для ввода числа с плавающей точкой
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField - поле для ввода даты и времени
    updated_at = models.DateTimeField(auto_now=True) # auto_now - поле, которое автоматически обновляется при каждом сохранении модели
    hashtags = models.ManyToManyField(
        HashTag, 
        related_name="posts"
    ) # ManyToManyField - поле для связи с другой моделью


    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        db_table = "post"
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(
        "post.Post",
        on_delete=models.CASCADE,
        related_name="comments" # related_name - имя, по которому можно получить все комментарии поста
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.id} - {self.text[:20]}'

