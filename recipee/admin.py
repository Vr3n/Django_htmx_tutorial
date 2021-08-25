from django.contrib import admin, auth
from .models import Recipe, RecipeIngredient

# Register your models here.
User = auth.get_user_model()


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    fields = ['name', 'quantity', 'unit', 'description']
    readonly_fields = ['quantity_in_float', 'as_mks', "as_imperial"]
    extra = 1

class RecipeIngredientAdmin(admin.ModelAdmin):
    readonly_fields = ['quantity_in_float', 'as_mks', "as_imperial"]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['created_on', 'updated_on']
    raw_id_fields= ['user']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)