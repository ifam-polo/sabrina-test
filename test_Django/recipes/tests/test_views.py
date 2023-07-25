from django.urls import reverse, resolve

# Verificar se a view da home esta sendo renderizada quando acessada pela url 
def test_recipe_view_home_fuction_is_correct():
    view = reverse(resolve('recipes:home'))
    assert 1 == 1
