from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FoodOrder

def order_list(request):
    orders = FoodOrder.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
