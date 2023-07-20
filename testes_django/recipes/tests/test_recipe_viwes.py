from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


    
class RecipeViewsTest(TestCase):
        # verificar se a view da home está sendo rederizada quando acessada pela url
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func.view_class, views.RecipeListViewHome)
        
    # verificar se a view da category está sendo rederizada quando acessada pela url 
    def test_recipe_category_function_is_correct(self):
       view = resolve(reverse('recipes:category', kwargs={'category_id':1}))
       self.assertIs(view.func.view_class, views.RecipeListViewCategory)
     
    # verificar se a view da detail está sendo rederizada quando acessada pela url  
    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'pk': 1}))
        self.assertIs(view.func.view_class, views.RecipeDetail)
        
        
    # verificar se a view da search está sendo rederizada quando acessada pela url
    def test_recipe_search_views_function_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func.view_class, views.RecipeListViewSearch)
        
    
    # retornar o status http correto para view
    def test_recipe_home_view_returns_status_code_200_ok(self):
            response = self.client.get(reverse('recipes:home'))
        
    
    
    