from django.shortcuts import render
from utils.recipes.recipes_generator import make_recipe
from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by("-id")
    return render(request, 'recipes/home.html', context={
        'recipes': recipes
    })


def recipe(request, recipe_id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
