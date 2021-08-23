from django.utils.text import slugify
from .models import Article

def slugify_instance_title(instance, save=False):
    slug = slugify(instance.title)
    qs = Article.objects.filter(slug=slug).exclude(id=instance.id)

    # if query exists then append the count.
    if qs.exists():
        slug = f"{slug}-{qs.count() + 1}"

    instance.slug = slug

    # This will be usefull in post save if you want to save the instance.
    if save:
        instance.save()

    return instance
