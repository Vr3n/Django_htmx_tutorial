from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Article
import random

# Create your views here.


def home(request):
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)
    queryset = Article.objects.filter()

    context = {"article_obj": article_obj, "queryset": queryset}

    return render(request, 'articles/home-view.html', context)

@login_required
def article_detail(request, slug):
    queryset = Article.objects.get(slug=slug)
    context = {"obj": queryset}
    return render(request, "articles/article-detail.html", context)


def article_search_view(request, *args, **kwargs):
    search_key = request.GET.get('q')
    queryset = Article.objects.search(search_key)
    context = {}

    if queryset.exists():
        context = {"obj": queryset}

    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    context = {}

    form = ArticleForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            article_obj = form.save()
            context['obj'] = article_obj
            context['created'] = True
    context['form'] = form

    return render(request, "articles/create.html", context)