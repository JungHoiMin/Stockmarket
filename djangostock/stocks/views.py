from django.shortcuts import render
import requests
import json


def home(request):
    stock_api = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_6ce1d6df0d3643219faa325f0d61129a")
    stock = json.loads(stock_api.content)

    content = {'stock':stock}

    return render(request, 'stocks/home.html', content)
