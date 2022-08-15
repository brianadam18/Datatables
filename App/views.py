from django.shortcuts import render
from App.models import Inventory
# Function to render Homepage
def home(request):
    inventory_list = Inventory.objects.all()
    return render(request, 'home.html', {"inventorys": inventory_list})
