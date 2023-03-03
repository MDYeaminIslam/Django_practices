#here we'll create a form
#now we'll use validators to validate specific field
from django.core import validators
from django import forms

class RecentProduct(forms.Form):
    #mobile = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput,) #widget is a class helps to change the input type. we can add this to give more instruction to the user. we can put this after widget parameter (min_length=8, max_length=20, error_messages={'required': 'Enter Your Password'})
    re_password = forms.CharField(widget=forms.PasswordInput,) 
    laptop = forms.CharField(label='Enter Your laptop Name ')#by doing this we can change the label name
    email = forms.EmailField(initial='yeamin.cse@gmail.com', label_suffix=' = ',validators=[validators.MaxLengthValidator(30)]) #here we use validators to validate the email field. we can use this validators in any field
    about = forms.CharField(help_text='Describe about your laptop')

    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':40}))#this will create a textarea. This attrs is a dictionary and it will take the value of rows and cols

    checkbox = forms.CharField(widget=forms.CheckboxInput())#this will create a checkbox and this widget helps to organize the form

    #Integer value
    ram = forms.IntegerField(min_value=4, max_value=10)
    #Decimal value
    ssd = forms.DecimalField(min_value=1,max_value=50,max_digits=3,decimal_places=2)
    #Boolean value
    youtube_channel = forms.BooleanField()


    #files = forms.CharField(widget=forms.FileInput())#this will create a file input

    #here we'll give manual instruction for the user password in function
    
    def clean_password(self):
        password_validation = self.cleaned_data['password'] #this will take the value of password

        #if condition meet then it will raise an error
        if len(password_validation)<4:
            raise forms.ValidationError('Enter your correct password')
        return password_validation
    

    #laptop validation manually
    def clean_laptop(self):
        laptop_validation = self.cleaned_data['laptop'] #this will take the value of password

        #if condition meet then it will raise an error
        if len(laptop_validation)<10:
            raise forms.ValidationError('Enter correct format')
        return laptop_validation


    #checking password and re_password
    def clean(self):
        cleaned_data = super().clean() #this will take the value of password and check the conditions of parent class
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match:
            raise forms.ValidationError('Password does not match')
        
