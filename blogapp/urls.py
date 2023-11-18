from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('<int:pk>/', SinBlogView.as_view(), name="sin_blog"),
]
