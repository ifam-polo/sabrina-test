from django.urls import reverse, resolve
from recipes import views
import pytest
from django.test import RequestFactory

# Verificar se a view da home esta sendo renderizada quando acessada pela url

def test_recipe_view_home_fuction_is_correct():
    view = resolve(reverse('recipes:home'))
    assert view.func.view_class is views.RecipeListViewHome

#verificar se o status code da view é 200
@pytest.mark.django_db
def test_recipe_home_view_returns_status_code_200_ok(client):
    response = client.get(reverse('recipes:home'))
    assert response.status_code == 200

 # Verificar se o template da home não tem receitas
@pytest.mark.django_db
def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(client):
        response = client.get(reverse('recipes:home'))
        assert ' <h1>No recipes found here 🥲</h1>' in response.content.decode('utf-8')

#Verificar se a view da category esta sendo renderizada quando acessada pela url
def test_recipe_view_category_fuction_is_correct():
    view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
    assert view.func.view_class is views.RecipeListViewCategory

#Verificar se a view da category esta sendo renderizada quando acessada pela url
def test_recipe_view_datail_fuction_is_correct():
    view = resolve(reverse('recipes:recipe', kwargs={'pk': 1}))
    assert view.func.view_class is views.RecipeDetail

#Verificar se a view da detail esta sendo renderizada quando acessada pela url

def test_recipe_view_search_fuction_is_correct():
    view = resolve(reverse('recipes:search'))
    assert view.func.view_class is views.RecipeListViewSearch


















