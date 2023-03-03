from django.shortcuts import render
#importing HttpResponseredirect from django.http and this will redirect to the url
from django.http import HttpResponseRedirect
from product.forms import RecentProduct
#from product app we are importing forms.py class RecentProduct()
from .models import laptop

#from django.http import HttpResponse
# Create your views here.

def product(request):
    return render(request,'product/product.html')

def details(request):
    if request.method == 'POST':
        frm = RecentProduct(request.POST)
        if frm.is_valid():

            '''
            This will print the form value in a dictionary
            in the terminal
            print("Form is valid")
            print(frm) 
            print('Password :',frm.cleaned_data['password']) this will print the form value in a dictionary
            print('Laptop',frm.cleaned_data['laptop']) this will print the form value in a dictionary
            print('Re-password :',frm.cleaned_data['re_password']) 
            print('Laptop :',frm.cleaned_data['laptop']) this will print the form value in a dictionary
            print('Email :',frm.cleaned_data['email']) 
            print('About :',frm.cleaned_data['about']) 
            print('Textarea :',frm.cleaned_data['textarea']) 
            print('Checkbox :',frm.cleaned_data['checkbox'])
            print('Ram :',frm.cleaned_data['ram'])  
            print('ssd :',frm.cleaned_data['ssd'])  
            print('Youtube_channel :',frm.cleaned_data['youtube_channel']) this will print the form value in a dictionary in the terminal
            
            
            '''

            pas = frm.cleaned_data['password']
            rpas = frm.cleaned_data['re_password']
            lap = frm.cleaned_data['laptop']
            eml = frm.cleaned_data['email']
            abt = frm.cleaned_data['about'] 
            txt = frm.cleaned_data['textarea'] 
            chk = frm.cleaned_data['checkbox']
            rm = frm.cleaned_data['ram']  
            ss = frm.cleaned_data['ssd']
            yt = frm.cleaned_data['youtube_channel'] 
            buy = laptop(password=pas,re_password=rpas,laptop=lap,email=eml,about=abt,textarea=txt,checkbox=chk,ram=rm,ssd=ss,youtube_channel=yt)
            #here we are creating an object of laptop class and passing the value of the form.Password represent the password field of the form and pas represent the value of the form
            buy.save() #saving the value in the database
            return HttpResponseRedirect('/product/successfully')
        

    else:
        #frm is an object
        frm = RecentProduct(auto_id=True, label_suffix=' - ') #taking value as string
        print("GET statement")



    
    #here we are going to order the form value by my choice and put it in a list
    #frm.order_fields(field_order=['email','laptop','mobile'])
    return render(request,'product/recent.html',{'from':frm})

def send(request):
    return render(request,'product/submit.html')