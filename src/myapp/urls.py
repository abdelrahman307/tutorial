"""
for every function created in views.py of an app ,
there must be a url created specially for that function 
for the user to reach it with 

"""

# a url for the index function in the views.py file :

from  django.urls import path   # path : a library to create a url for every function
from  . import views  # to call views.py to find the function and create a url for it

urlpatterns = [
    path('index' , views.index , name = 'index'),
    path('about' , views.about , name = 'about'),
]