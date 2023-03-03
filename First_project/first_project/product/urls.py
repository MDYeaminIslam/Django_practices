from django.urls import path
from . import views
urlpatterns = [
    path('', views.product, name='product'),
    path('recent/',views.details),
    path('successfully/',views.send),

    
]