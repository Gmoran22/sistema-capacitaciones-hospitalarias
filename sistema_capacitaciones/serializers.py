from rest_framework import serializers
from .models import Capacitado

class CapacitadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitado
        # El '__all__' le dice a Django que incluya todos los campos de la tabla automáticamente
        fields = '__all__'