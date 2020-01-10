from django.urls import path
from . import views

urlpatterns = [
    path('insert1',       views.insert1,        name='insert1'),
    path('select1',       views.select1,        name='select1'),
    path('select_m',       views.select_m,        name='select_m'),
    path('select3',       views.select3,        name='select3'),







]
