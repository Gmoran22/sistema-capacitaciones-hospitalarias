from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_capacitado_view, name='registro_capacitado'),
    path('exito/', views.registro_exitoso_view, name='registro_exitoso'),
    path('exportar-excel/', views.exportar_excel_view, name='exportar_excel'),
]