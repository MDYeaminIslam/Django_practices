import datetime
from django.shortcuts import render
#importing payment model from payment_models
from payment.models import pay_method

#from django.http.response import HttpResponse

# Create your views here.

def bk(request):
    #this are the variable
    # d = datetime().datetime.now()
    
    payments_method = 'Bkash'
    discount = '50%'
    #condition = 'Only first payment'
    #variables are stored in dictionary
    payments_details = {'pm':payments_method, 'dis': discount}
    names = {'friends':['Yeamin','Aiyub','shohidul','Shourov','Tarif']}

    return render(request,'payment/payments-1.html', names)
    #here render basically takes two arguments one is request and another is template name and it takes output value from template and return it to browser.

def rk(request):
    return render(request,'payment/payments-2.html')

def payment_method(request):
    pay_m = pay_method.objects.all() #copy all the query set from pay_method class
    return render(request,'payment/pay.html',{'pay': pay_m})