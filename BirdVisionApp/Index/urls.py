from django.urls import  path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomePage, name='Homepage'),
    path('chat/', views.chatbot, name='ChatBot'),
]