from . import views
from django.urls import path 

urlpatterns = [
    path('',views.index,name='index'),
    path('display',views.display,name='display'),
    path('display/data/<int:id>',views.staff,name='staff')
]
