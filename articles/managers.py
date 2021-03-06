from django.db import models
from django.db.models import Q


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()

        return self.filter(Q(title__icontains=query) | Q(content__icontains=query)) 

class ArticleManager(models.Manager):

    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)