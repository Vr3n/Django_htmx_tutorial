from django.db import models
from django.utils.text  import  slugify
import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publish_date = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
