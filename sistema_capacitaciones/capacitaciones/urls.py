from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_capacitado_view, name='registro_capacitado'),
    path('exito/', views.registro_exitoso_view, name='registro_exitoso'),
    path('exportar-excel/', views.exportar_excel_view, name='exportar_excel'),
    
    # Endpoint GET para el padrón
    path('api/padron/', views.PadronActivoListView.as_view(), name='padron_activo'),

    # Rutas del frontend
    path('registro-qr/', views.registro_qr_view, name='registro_qr'),
    path('generador-qr/', views.generador_qr_view, name='generador_qr'),
    path('padron-live/', views.padron_live_view, name='padron_live'),
    path('busqueda-rapida/', views.busqueda_rapida_view, name='busqueda_rapida'),
    path('guardado-offline/', views.guardado_offline_view, name='guardado_offline'),
    path('sincronizacion/', views.sincronizacion_view, name='sincronizacion'),
]