import requests
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .forms import RegisterForm,Weatherform
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def welcome(request):
    return render(request,'weather/welcome.html')

#creating view for register_user
def Register_view(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            login(request,user)
            return redirect('/weather')
    else:
        form = RegisterForm()
    return render(request,'weather/register.html',{'form':form})        
            
            
            
            
            
#view for the login
def login_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request,'Login Sucessful')
                return redirect('/weather')
            else:
                messages.error(request,'invalid username or password')
        else:
            messages.error(request,'invlad username or password')
    else:
        form = AuthenticationForm()
        
    return render(request,'weather/login.html',{'form':form})                    
            
            
            
@login_required
def Weather(request):   
    weather_data = None
    if request.method =="POST":
        form = Weatherform(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = "f48a41c19591483fb6f54354252403"
            api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"  
            
            try:
                response = requests.get(api_url)
                data = response.json()
                if 'error' in data:
                    messages.error(request,'Invalid city name')
                    
                else:
                    weather_data = {
                        "city":data['location']['name'],
                        "temperature":data['current']['temp_c'],
                        "description":data['current']['condition']['text'],
                        "humidity":data['current']['humidity'],
                        "wind_speed":data['current']['wind_kph'],
                        "icon":data['current']['condition']['icon']
                    }           
            except requests.exceptions.RequestException:
                messages.error(request, "Error fetching weather data. Please try again!")
                
    else:
        form = Weatherform()
    return render(request,'weather/weather.html',{'form':form,'weather_data':weather_data})                
            
            
#log out view
def logout_view(request):
    logout(request)
    return redirect('/login')               