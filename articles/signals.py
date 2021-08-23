from django.db.models.signals import pre_save, post_save

from .utils import slugify_instance_title
from .models import Article


def article_pre_save(sender, instance, *args, **kwargs): 
    if instance.slug is None:
        slugify_instance_title(instance)



pre_save.connect(article_pre_save, sender=Article)