from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Recipe, RecipeIngredient

# Create your tests here.

User = get_user_model()


# class UserTestCase(TestCase):

#     def test_user_pw(self):
#         checked = self.user_a.check_password("abc123")
#         self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('virus', password="abc123")
        self.recipe_a = Recipe.objects.create(user=self.user_a, name="Shwarma")
        self.recipe_b = Recipe.objects.create(
            user=self.user_a, name="Butter Chicken")

        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe=self.recipe_a, name="chicken", quantity="1/2", unit="pounds")

        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe=self.recipe_a, name="butter", quantity="askdjsakj", unit="pounds")

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        print(qs)
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        print(qs)
        self.assertEqual(qs.count(), 2)

    def test_ingredient_recipe_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
        print(qs)
        self.assertEqual(qs.count(), 2)

    def test_ingredient_recipe_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        print(qs)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        print(qs)
        self.assertEqual(qs.count(), 2)

    def test_unit_measure_validation_error(self):
        invalid_unit = "donut"
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                name="New",
                quantity=10,
                recipe=self.recipe_a,
                unit=invalid_unit
            )
            ingredient.full_clean()

    def test_unit_measure_validation_success(self):
        valid_unit = "ounces"
        ingredient = RecipeIngredient(
            name="New",
            quantity=10,
            recipe=self.recipe_a,
            unit=valid_unit
        )
        ingredient.full_clean()

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_in_float)
        self.assertIsNone(self.recipe_ingredient_b.quantity_in_float)