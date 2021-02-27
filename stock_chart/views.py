from django.shortcuts import render


def chart(request):
    return render(request, 'stock_chart/chart.html')
