from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
import random

def main(request):
    all_recipes = list(Recipe.objects.all())
    recipes = random.sample(all_recipes, min(10, len(all_recipes)))
    return render(request, 'main.html', {'recipes': recipes})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'category_detail.html', {
        'category': category,
        'recipes': recipes
    })
