from django.urls import path
from bookstore import views
urlpatterns = [
    path('',views.index, name='form'),
    path('about/',views.about),
    path('form/',views.form),
    path('index', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart_view/',views.cart_view, name='cart_view'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'), 
    path('search/',views.search, name='search'),
    path('edit/<int:pk>/',views.edit, name='edit'),
    path('delete/<int:pk>/',views.delete, name = 'delete'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]