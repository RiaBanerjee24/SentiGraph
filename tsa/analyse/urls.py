from django.urls import path
from . import views

app_name = 'analyse'

urlpatterns = [
    path('', views.get, name='home'),
    path('results/',views.post, name='results'),
]
