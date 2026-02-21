from django.urls import path
from .views import orr_list
urlpatterns = [
    path('',orr_list,name='orr_list'),
]
