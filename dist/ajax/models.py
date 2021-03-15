from django.db import models


class Post(models.Model):
    title = models.CharField('タイトル', max_length=255)

    def __str__(self):
        return self.title


class InputRecord(models.Model):
    input_str = models.CharField('input_str', max_length=512)
    type_str = models.CharField('type_str', max_length=32)
    username_str = models.CharField('username_str', max_length=128)
    dt_str = models.CharField('dt_str', max_length=128)
    x_str = models.CharField('x_str', max_length=16)
    y_str = models.CharField('y_str', max_length=16)

    def __str__(self):
        return self.input_str

