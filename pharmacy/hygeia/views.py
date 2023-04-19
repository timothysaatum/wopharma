from django.shortcuts import render



def home(request):
	return render(request, 'hygeia/index.html')


def store(request):
	return render(request, 'hygeia/store.html')



def details(request):
	return render(request, 'hygeia/details.html')


def cart(request):
	return render(request, 'hygeia/cart.html')