from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('chefs/', ChefsView.as_view(), name="chefs"),
    path('elements/', ElementsView.as_view(), name="elements"),
    path('contact/', ContactView.as_view(), name="contact"),
]