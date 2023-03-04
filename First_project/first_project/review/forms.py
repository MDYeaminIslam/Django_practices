from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#here we'll inherit the UserCreationForm to edit the form accordin to our interested feilds.


class BuildingAdd(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']