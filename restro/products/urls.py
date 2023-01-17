from django.urls import path
from products.views import *

urlpatterns = [
 
    path('getallproduct/', GetAllProduct.as_view(), name='getallproduct'),
    path('getproductbyid/<int:id>', GetProductById.as_view(), name='getproductbyid'),
    path('product/next/<int:LIMIT>', ProductPaginatioNext.as_view(), name='productpaginationnext'),
    path('product/previous/<int:LIMIT>', ProductPaginationPrevious.as_view(), name='productpaginationprev'),

    path('getproductbycategory/<int:id>', GetProductByCategory.as_view(), name='getproductbycategory'),
    path('getallcategory', GetAllCategory.as_view(), name='getallcategory'),
    path('category/next/<int:LIMIT>', CategoryPaginatioNext.as_view(), name='categorypaginationnext'),
    path('category/previous/<int:LIMIT>', CategoryPaginationPrevious.as_view(), name='categorypaginationprev'),

    path('filter/',FilterProduct.as_view(), name='prev'),
]