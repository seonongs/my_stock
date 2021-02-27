from django.shortcuts import render


def home(request):
    return render(request, 'stock_home/home.html')
