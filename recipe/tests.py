from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewsTests(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Супи')
        self.category2 = Category.objects.create(name='Салати')
        for i in range(15):
            Recipe.objects.create(title=f'Рецепт {i}', instructions='...', category=self.category1)

    def test_main_view_returns_10_random_recipes(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn('recipes', response.context)
        self.assertLessEqual(len(response.context['recipes']), 10)

    def test_category_detail_view_returns_recipes_by_category(self):
        response = self.client.get(reverse('category_detail', args=[self.category1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        self.assertIn('recipes', response.context)
        self.assertEqual(len(response.context['recipes']), 15)
        self.assertEqual(response.context['category'].id, self.category1.id)

    def test_category_detail_404_for_invalid_id(self):
        response = self.client.get(reverse('category_detail', args=[999]))
        self.assertEqual(response.status_code, 404)