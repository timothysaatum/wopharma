from django.urls import path
from . import views


urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('store/', views.store, name='store'),
	path('items/details/<int:pk>/', views.DrugDetailView.as_view(), name='details'),
	path('purchase/<str:category>/<str:drug>/<int:pk>/', views.purchase_item, name='purchase-item'),
	path('pharmacy/details/<int:pk>/', views.PharmacyDetail.as_view(), name='pharmacy-details'),
	path('item/add-to-cart/', views.cart, name='cart'),
    path('how-is-works/', views.how_is_work, name='works'),
    path('add/pharmacy/', views.PharmacyStore.as_view(), name='add-pharmacy'),
    path('add/drug/category/', views.CreateDrugCategory.as_view(), name='add-drug-category'),
    path('add/drug/', views.CreateDrug.as_view(), name='add-drug'),
    path('pharmacy/update/info/<int:pk>/', views.UpdatePharmacyInfo.as_view(), name='update-pharmacy-info'),
    path('drug/category/update/info/<int:pk>/', views.UpadteDrugCateforyInfo.as_view(), name='update-category-info'),
    path('drug/update/info/<int:pk>/', views.UpdateDrugInfo.as_view(), name='update-drug-info')
]