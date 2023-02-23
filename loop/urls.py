from django.urls import path
from .views import *


urlpatterns = [
    path('', LoopIndex.as_view(), name='index'),
    path('<int:category_id>/', LoopCategory.as_view(), name='category'),
    # path('add/', ProductAdd.as_view(), name='add'),
    path('detail/<int:id>/', detail, name='detail'),
    path('new/', CategoryNew.as_view(), name='category_stock'),
    path('price_lt/', CategoryPrice.as_view(), name='price_lt'),
    path('delivery/', delivery, name='delivery'),
]

