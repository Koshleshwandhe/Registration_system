from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('main/', views.main_screen, name='main_screen')
    
]
