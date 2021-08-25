from django.contrib import admin, auth
from .models import Recipe, RecipeIngredient

# Register your models here.
User = auth.get_user_model()


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    # fields = ['name', 'quantity', 'unit', 'description']
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['created_on', 'updated_on']
    raw_id_fields= ['user']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)