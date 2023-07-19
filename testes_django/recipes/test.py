from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):
        
    def test_recipe_home_url_is_correct(self):
        #Verificação de correspondencia da url home
        home_url = reverse('recipes:home')
        self.assertAlmostEqual(home_url, '/')
        
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1} )
        self.assertEqual(url, '/recipes/category/1/')
        
    