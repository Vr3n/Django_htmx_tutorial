from django import forms

from .models import Recipe, RecipeIngredient

# Create your forms here.

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
