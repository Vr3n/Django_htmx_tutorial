from django.utils.text import slugify

import random
from .models import Article

def slugify_instance_title(instance, save=False, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    # get the class of instance for query
    qs_class = instance.__class__
    qs = qs_class.objects.filter(slug=slug).exclude(id=instance.id)

    # if query exists then append the count.
    if qs.exists():
        slug = f"{slug}-{random.randint(1000,99999)}"
        return slugify_instance_title(instance, new_slug=slug)

    instance.slug = slug

    # This will be usefull in post save if you want to save the instance.
    if save:
        instance.save()

    return instance
