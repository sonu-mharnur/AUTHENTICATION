from django.urls import path
from .import views


urlpatterns = [
    
    path('signup/', views.register, name='register'),
] 

    
LOGIN_REDIRECT_URL = '/'