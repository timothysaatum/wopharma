from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'),
	path('store/', views.store, name='store'),
	path('items/details', views.details, name='details'),
	path('item/add-to-cart', views.cart, name='cart'),
    path('how-is-works', views.how_is_work, name='works')
]