###  this is called urlconfig
# urlpatterns = [
# 	path('hello/', views.say_hello)
# ]

from . import views
from django.urls import path

urlpatterns = [
	path('hello/', views.say_hello)
]


