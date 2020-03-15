import json
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

IMG = "no.webp"
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    json_url = urlopen("https://api.duckduckgo.com/?q="+search+"&format=json&pretty=1")
    print("https://api.duckduckgo.com/?q="+search+"&format=json&pretty=1")
    data = json.loads(json_url.read())
# Starting of the new Section
    # soup = BeautifulSoup(data, features='html.parser')
# Ending of the new Section
    context = {
    	'data': data,
        'IMGURL': IMG,
    }
    return render(request, 'myapp/new_search.html', context)