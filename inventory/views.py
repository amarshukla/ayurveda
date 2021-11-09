from django.shortcuts import render
from .models import Inventory
# Create your views here.
def index(request):
    context = {'meds_list': Inventory.objects.all()}
    return render(request, 'inventory/index.html', context)