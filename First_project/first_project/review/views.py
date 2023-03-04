from django.shortcuts import render
from django.http import HttpResponse
#for creating userform automatically which we did in manually in product apps
from .forms import BuildingAdd
# Create your views here.

def customer(request):
    return render(request,'review/review.html')


def building_form(request):
    if request.method == 'POST':
        frm = BuildingAdd(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = BuildingAdd
    return render(request,'review/building.html',{'form':frm})