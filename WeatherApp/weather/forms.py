from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
#create forms here

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password1','password2']
        
        
        
#creatingi a form for getting input city for the weather search
class Weatherform(forms.Form):
    city = forms.CharField(label='Enter City', max_length=100)        
        
