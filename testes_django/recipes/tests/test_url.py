
from django.urls import reverse



def test_home_url_is_correct():
    url = reverse("recipes:home")
    assert url == '/'
    
def test_category_url_is_correct():
    url = reverse('recipes:category', kwargs={'category_id': 1})
    assert url == '/recipes/category/1/'