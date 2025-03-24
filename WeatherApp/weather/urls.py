from django.urls import path
from . import views
urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('register/',views.Register_view,name='Register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name="logout"),
    path('weather/',views.Weather,name='weather')
]
