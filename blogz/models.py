from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    title = models.SlugField("Метка", max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField("Название", max_length=250)
    description = models.CharField("Краткое описание", max_length=300)
    text = models.TextField("Текст статьи")
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created = models.DateTimeField("Время создания", auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
