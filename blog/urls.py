from django.urls import path
from . import views 

blog_patterns = ([
    #Paths del core
    path('', views.PostListView.as_view(), name='blogs'),
    #Path de las categorias
    path('<slug:slug>', views.PostDetailView, name='posts'),
    path('category/<int:category_id>/', views.CategoryListView.as_view(), name='category'), #El <category_id> es una cadena de caracteres y el int se utiliza para convertirlo a numero entero
], 'blog')