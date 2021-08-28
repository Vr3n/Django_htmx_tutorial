import pdb 
from django.shortcuts import reverse, render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.forms.models import modelformset_factory

from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm

# Create your views here.

# CRUD VIEWS FOR Recipe.

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.all()
    context = {
        'obj': qs
    }

    return render(request, 'recipee/list.html', context)

@login_required
def recipe_detail_view(request, id):
    hx_url = reverse('recipes:hx-detail', kwargs={"id": id})
    context = {
        'hx_url': hx_url
    }
    return render(request, "recipee/detail.html", context)

@login_required
def recipe_update_view(request, id=None):
    recipe_instance = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=recipe_instance)
    form_2 = RecipeIngredientForm(request.POST or None)
    RecipeIngredientFormset = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=1)

    qs = recipe_instance.recipeingredient_set.filter()
    formset = RecipeIngredientFormset(request.POST or None, queryset=qs)

    context = {}
    context['form'] = form
    context['form_2'] = formset

    if form.is_valid() and formset.is_valid():
        recipe_instance = form.save()
        for form in formset:
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe_instance
            ingredient.save()
            messages.success(request, "Recipe was updated successfully")

    if form.is_valid() != True:
        messages.error(request, form.errors)

    if request.htmx:
        return render(request, 'partials/form.html', context)

    return render(request, 'recipee/create-update.html', context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {}
    context['form'] = form

    if form.is_valid():
        recipe_instance = form.save(commit=False)
        recipe_instance.user = request.user
        recipe_instance.save()
        context['obj'] = recipe_instance
        messages.success(request, "Recipe was updated successfully")

    if request.htmx:
        return render(request, 'partials/form.html', context)

    return render(request, 'recipee/create-update.html', context)


@login_required
def recipe_detail_hx_view(request, id):

    try:
        obj = Recipe.objects.get(id=id)
    except:
        obj = None
    
    if obj is None:
        return HttpResponse("Recipe Not Found")


    context = {
        'obj': obj
    }
    return render(request, "partials/detail.html", context)

@login_required
def recipe_search_view(request, id):

    try:
        obj = Recipe.objects.get(id=id)
    except:
        obj = None
    
    if obj is None:
        return HttpResponse("Recipe Not Found")


    context = {
        'obj': obj
    }
    return render(request, "recipee/search.html", context)
