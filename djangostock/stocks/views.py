from django.shortcuts import render
import requests
import json


def home(request):
    try:
        ticker = request.GET['ticker']
        stock_api = requests.get(
            f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_6ce1d6df0d3643219faa325f0d61129a")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""

    content = {'stock': stock}

    return render(request, 'stocks/home.html', content)
