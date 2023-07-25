
from django.urls import reverse


 #Verificação de correspondencia da url home 
def test_home_url_is_correct():
    url = reverse("recipes:home")
    assert url == '/'
    
 #Verificação de correspondencia da url category
def test_category_url_is_correct():
    url = reverse('recipes:category', kwargs={'category_id': 1})
    assert url == '/recipes/category/1/'
    
 #Verificação de correspondencia da url detail   
def test_detail_url_is_correct():
     url = reverse('recipes:recipe', kwargs={'pk':1})
     assert url == '/recipes/1/'
     
     
 #Verificação de correspondencia da url search
def test_search_url_is_correct():
    url = reverse('recipes:search')
    assert url == '/recipes/search/'   
     