from django.urls import path
from . import views


urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('store/', views.store, name='store'),
	path('items/details/<int:pk>', views.DrugDetailView.as_view(), name='details'),
	path('item/add-to-cart/', views.cart, name='cart'),
    path('how-is-works/', views.how_is_work, name='works'),
	path('upload-prescription/', views.upload_prescription, name='prescription')
]