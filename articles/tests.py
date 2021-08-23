from django.test import TestCase
from django.utils.text import slugify

from .utils import slugify_instance_title
from .models import Article

# Create your tests here.

class ArticleTestCase(TestCase):

    def setUp(self):

        self.number_of_articles = 100

        for i in range(0, self.number_of_articles):
            Article.objects.create(title="Hello, Friend", content="testing the db")

    # to make sure articles exist in db.
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs_count = Article.objects.all().count()
        self.assertEqual(qs_count, self.number_of_articles)

    def test_slug(self):
        obj = Article.objects.all().first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)

    def test_unique_slug(self):
        qs = Article.objects.exclude(slug__iexact="hello-world")
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slugified_title, title)

    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slugs = []

        for i in range(0, 25):
            instance = slugify_instance_title(obj)
            new_slugs.append(instance.slug)

        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_slugify_instance_title_util(self):
        slugs = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slugs))
        self.assertEqual(len(slugs), len(unique_slug_list))

    def test_user_entered_slug_unique(self):
        user_slug = "new-slug"
        qs = Article.objects.all()

        for obj in qs:
            self.assertNotEqual(user_slug, obj.slug)

    def test_user_entered_slug_not_unique(self):
        user_slug = "hello-world"
        qs = Article.objects.all()

        for obj in qs:
            self.assertNotEqual(user_slug, obj.slug)