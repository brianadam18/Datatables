from django.shortcuts import render
from App.models import Inventory
from django.http import JsonResponse
# Function to render Homepage
def home(request):
    return render(request, 'home.html')

#JSON
def inventory_json(request):
    inventory = Inventory.objects.all()
    data = [inventory.get_data() for inventory in inventory]
    responese = {'data': data}
    return JsonResponse(responese)

