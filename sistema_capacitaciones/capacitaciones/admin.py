from django.contrib import admin
from django.urls import reverse
from .models import Capacitado

@admin.register(Capacitado)
class CapacitadoAdmin(admin.ModelAdmin):
    list_display = (
        'cuil', 'apellido', 'nombre', 'profesion', 'categoria',
        'tipo_usuario', 'servicio', 'area_trabajo', 'material_enviado', 'fecha_registro'
    )
    search_fields = ('cuil', 'apellido', 'nombre', 'mail_personal', 'correo_gcba')
    list_filter = ('tipo_usuario', 'categoria', 'tipo_matricula', 'servicio', 'material_enviado')
    
    # Orden descendente por defecto (más recientes primero)
    ordering = ('-fecha_registro',)
    
    # Permite tildar 'material_enviado' directo desde la grilla
    list_editable = ('material_enviado',)
    
    # 'fecha_registro' es generada por el sistema
    readonly_fields = ('fecha_registro',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['exportar_url'] = reverse('exportar_excel')
        return super().changelist_view(request, extra_context=extra_context)