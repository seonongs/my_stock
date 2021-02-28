from django.shortcuts import render

from stock_chart.stock_data import dataTest, samsung_tests


def chart(request):
    return render(
        request, 'stock_chart/chart.html', {'samsung_tests': samsung_tests})
