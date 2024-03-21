from django.urls import path
from . import views 

urlpatterns = [ 
    path('FeedBack/', views.FeedBack,  name='FeedBack'), 
]