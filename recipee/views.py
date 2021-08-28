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

    context = {}
    context['form'] = form
    context['object'] = recipe_instance

    if form.is_valid():
        recipe_instance = form.save()
        messages.success(request, "Recipe Updated successfully")

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

@login_required
def recipe_ingredient_detail_hx_view(request, parent_id=None,id=None):
    if not request.htmx:
        raise Http404
    try:
        obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        obj = None

    if obj is None:
        return HttpResponse("Recipe Not Found")

    if obj is None:
        return HttpResponse("Not Found.")

    instance = None

    if id is not None: 
        try:
            instance = RecipeIngredient.objects.get(recipe=parent_id, id=id)
        except:
            instance = None

    form = RecipeIngredientForm(request.POST or None, instance=instance)
    context = {
        'object': instance,
        'form': form
    }

    url = instance.get_hx_edit_url() if instance else reverse('recipes:hx-ingredient-new', kwargs={
        "id": obj.id
    })

    if form.is_valid():
        new_obj = form.save(commit=False)

        if instance is None:
            new_obj.recipe = obj
        new_obj.save()
        context['object'] = context
        return render(request, "partials/ingredient-form.html", context)

    return render(request, "partials/ingredient-inline.html", context)
