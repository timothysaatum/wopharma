from django.urls import path
from . import views


urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('store/', views.store, name='store'),
	path('items/details/<int:pk>', views.DrugDetailView.as_view(), name='details'),
	path('item/add-to-cart/', views.cart, name='cart'),
    path('how-is-works/', views.how_is_work, name='works'),
	path('upload-prescription/', views.upload_prescription, name='prescription'),
	path('herbal-medicine/', views.herbal_medicine, name='herbals'),
	path('sundries/', views.sundries, name='sundries'),
	path('cosmetics/', views.cosmetics, name='cosmetics'),
	path('vitamins/', views.vitamins, name='vitamins'),
	path('snacks-confec/', views.snacks_confec, name='snacks'),
	path('baby-food/', views.baby_food, name='baby'),
	path('sex-enhance/', views.sex_enhance, name='sex'),
	path('pharmacies/', views.pharmacies, name='pharmacies'),
	path('book-consult/', views.book_consult, name='consultation'),
	path('drug-details/', views.drug_details_page, name='drug'),
	path('checkout/', views.checkout, name='checkout'),
	path('cart-page/', views.cart_page, name='cart-page'),
	path('consultation/', views.consultation, name='consult'),
	path('specialist/', views.specialist, name='specialist'),
	path('contact-us/', views.contact_us, name='contact'),
	path('faqs/', views.faqs, name='questions'),
	path('services/', views.service, name='service'),
	path('about-us/', views.about, name='about'),
	path('mission/', views.mission, name='mission'),
	path('how-it-works/', views.works, name='works'),
	path('complaint/', views.complaint, name='works'),
	path('delivery/', views.delivery, name='delivery'),
	path('data-handling/', views.data, name='data')
]