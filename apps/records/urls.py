from django.contrib import admin
from django.urls import path
from .views import index,records,add_gasto,investimentos,fixos,parcelas,planejamento

urlpatterns = [
    path('', index, name="index" ),
    path('records',records,name="records"),
    path('add_gasto',add_gasto,name="add_gasto"),
    path('investimentos',investimentos,name="investimentos"),
    path('fixos',fixos,name="fixos"),
    path('parcelas',parcelas,name="parcelas"),
    path('planejamento',planejamento,name="planejamento"),
]