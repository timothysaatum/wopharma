from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drug, Pharmacy, DrugCategory
from django.views.generic import (TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView)
from .forms import PharmacyCreationForm
from django.urls import reverse_lazy
#from django.contrib import messages




class HomeView(ListView):
	model = Drug
	template_name = 'hygeia/index.html'
	context_object_name = 'drugs'


	def get_context_data(self, **kwargs):

		context = super(HomeView, self).get_context_data(**kwargs)
		context['vitamins'] = Drug.objects.filter(tag__tag='vitamins & supplements')
		context['baby_food'] = Drug.objects.filter(tag__tag='baby food')
		context['sex_drugs'] = Drug.objects.filter(tag__tag='sex enhancers')
		context['cosmetics'] = Drug.objects.filter(tag__tag='cosmetics')

		print(context)

		return context


def store(request):
	return render(request, 'hygeia/store.html')



class DrugDetailView(DetailView):
	model = Drug
	template_name = 'hygeia/drug_details.html'

def cart(request):
	return render(request, 'hygeia/cart.html')

def how_is_work(request):
	return render(request, 'hygeia/how_is_works.html')


class PharmacyStore(LoginRequiredMixin, CreateView):
	model = Pharmacy

	form_class = PharmacyCreationForm
	template_name = 'hygeia/pharmacy_create.html'
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.owner = self.request.user

		return super().form_valid(form)




class CreateDrugCategory(LoginRequiredMixin, CreateView):
	model = DrugCategory

	#form_class = DrugCategoryCreationForm
	template_name = 'hygeia/drug_category.html'
	success_url = reverse_lazy('home')
	fields = '__all__'


class CreateDrug(LoginRequiredMixin, CreateView):
	model = Drug
	template_name = 'hygeia/drug.html'
	success_url = reverse_lazy('home')
	fields = '__all__'


class UpdatePharmacyInfo(LoginRequiredMixin, UpdateView):
	model = Pharmacy

	template_name = 'hygeia/pharmacy_update.html'

	fields = '__all__'

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(owner=self.request.user)

	def get_success_url(self):
		return reverse('home')




class UpadteDrugCateforyInfo(LoginRequiredMixin, UpdateView):
	model = DrugCategory

	template_name = 'hygeia/category_update.html'

	fields = '__all__'

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(pharmacy__owner=self.request.user)

	def get_success_url(self):
		return reverse('home')


class UpdateDrugInfo(LoginRequiredMixin, UpdateView):
	model = Drug

	template_name = 'hygeia/drug_update.html'

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(category__pharmacy__owner=self.request.user)



class PharmacyDetail(LoginRequiredMixin, DetailView):
	model = Pharmacy
	template_name = 'hygeia/pharmacy_details.html'
