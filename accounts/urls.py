from django.urls import path
from .views import *

urlpatterns = [
    
   path('register/', register_user),
   path('login/',login_form),
   path('logout/',logout_user)
   
]
