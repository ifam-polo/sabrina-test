from django.test import TestCase
from django.urls import reverse

class RecipeURLsTest(TestCase):
     
    #Verificação de correspondencia da url home   
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertAlmostEqual(home_url, '/')
        
        
    #Verificação de correspondencia da url category
    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1} )
        self.assertEqual(url, '/recipes/category/1/')
    
    #Verificação de correspondencia da url detail    
    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse('recipes:recipe', kwargs={'pk': 1})
        self.assertEqual(detail_url, '/recipes/1/')
        
    #Verificação de correspondencia da url detail 
    def test_recipe_search_url_is_correct(self):
        search_url = reverse('recipes:search')
        self.assertEqual(search_url, '/recipes/search/')
        
        
    #verificar se o status code da url da view é 200
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    
    