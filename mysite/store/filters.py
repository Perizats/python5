from django_filters import FilterSet
from .models import Product, Category


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category' : ['exact'],
            'have' : ['exact'],
            'price' : ['gt', 'lt']
        }

class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = {
            'category_name': ['exact']
        }