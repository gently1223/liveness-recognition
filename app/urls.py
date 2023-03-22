from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', fnSignup, name="startwebcam"),
    path('signin/', fnLogin, name="signin")
]