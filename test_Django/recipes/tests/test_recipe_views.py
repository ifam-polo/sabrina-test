from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


    
class RecipeViewsTest(TestCase):
        # verificar se a view da home está sendo renderizada quando acessada pela url
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func.view_class, views.RecipeListViewHome)
    
    #verificar se o status code da view é 200    
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    #Verificar se esta renderizando o templete certo
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    # Verificar se o template da home não tem receitas
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            ' <h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8'))
        
            
    # verificar se a view da category está sendo renderizada quando acessada pela url 
    def test_recipe_category_view_function_is_correct(self):
       view = resolve(reverse('recipes:category', kwargs={'category_id':1}))
       self.assertIs(view.func.view_class, views.RecipeListViewCategory)   
       
    # Verificar se o template da category retorna 404 // problema
   # def test_recipe_category_view_return_status_code_404_if_no_recipes_found(self):
    #    response = self.client.get(reverse('recipes:category', kwargs={'category_id': 100}))
     #   self.assertEqual(response.status_code, 404)
       
        
    # verificar se a view da detail está sendo renderizada quando acessada pela url  
    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'pk':1}))
        self.assertIs(view.func.view_class, views.RecipeDetail)
        
        
    # verificar se a view da search está sendo renderizada quando acessada pela url
    def test_recipe_search_views_function_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func.view_class, views.RecipeListViewSearch)
        
    # verificar se a view da search está retornando 404
  #  def test_recipe_detail_views_return_404_if_no_recipes_found(self):
   #     response = self.client.get((reverse('recipes:recipe', kwargs={'pk':1})))
    #    self.assertEqual(response.status_code, 404)
        
