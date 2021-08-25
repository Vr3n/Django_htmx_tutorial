from django.db import models
from django.contrib.auth import get_user_model
import datetime

from .managers import ArticleManager

User = get_user_model()

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(unique=True,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = ArticleManager()

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"