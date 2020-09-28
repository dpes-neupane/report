from django.shortcuts import render
from .models import *

from django.http import HttpResponse
from .calculation import calculator

from django.shortcuts import render

def index(request):
    
    
    years = [(2010,2014), (2005,2009),  (2000,2004)]
    products = []
    all_values = []
    
    for p in Product.objects.all():
        products.append(p.product)
    for p in products:
        for y in years:
            val = calculator(y[0],y[1], p)
            if val != []:
                all_values.append([p,y, min(val), max(val), sum(val)/len(val)]) #adding the min, max and the avg of the given ineterval years and the respective product
            else:
                all_values.append([p, y, 0, 0, 0]) #if no value is returned then the products have zero sale for the given interval
            
    context = {'all_values' : all_values}

    return render(request, 'petroleum_report/index.html', context)