from  django.urls import path
from .views import ProductViewSet, CategoryViewSet


urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list',
                                     'post': 'create' }), name='product_list'),

    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete' : 'destroy'}), name='product_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='category_list'),

]
