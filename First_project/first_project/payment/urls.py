from django.urls import path
from . import views
urlpatterns = [
    #path('', views.name),
    #path('bk/', views.bkash),
    #path('add/', views.add),
    #path('home_page/', views.home_page),
    #here name is a keyword argument and it is used to give a name to the url and also works as a context which we passed at the url of base file.
    path('bkash/', views.bk, name='paymentone'),
    path('rocket/',views.rk,name='paymenttwo'),
    path('pays/',views.payment_method),
]