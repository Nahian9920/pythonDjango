from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyCost

# Create your views here.
#return HttpResponse("<span>current...")
def home(request):
    all_expense = DailyCost.objects.all()
    return render(request, 'index.html', {'all_data': all_expense})
    #return HttpResponse("123")

def me(request):
    return render(request,'about.html')
def my_expenses(request):
    all_expense = DailyCost.objects.all()
    return render(request, 'about.html',{'my_expense':all_expense})



