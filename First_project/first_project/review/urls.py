from django.urls import path
from . import views
urlpatterns = [
    path('', views.customer,name='review'),
    path('build/',views.building_form),

]