import re
from django import forms
from .models import Capacitado

class CapacitadoForm(forms.ModelForm):
    sitio_web = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Capacitado
        fields = [
            'tipo_usuario', 'tiene_acceso_sigehos', 'trabaja_otro_hospital',
            'permisos_solicitar', 'apellido', 'otro_apellido', 'nombre', 'otro_nombre',
            'cuil', 'correo_gcba', 'mail_personal', 'telefono',
            'profesion', 'tipo_matricula', 'numero_matricula', 'especialidad',
            'servicio', 'dias_horarios', 'area_trabajo', 'categoria'
        ]
        widgets = {
            'tipo_usuario': forms.Select(attrs={'class': 'form-select'}),
            'permisos_solicitar': forms.Select(attrs={'class': 'form-select'}),
            'trabaja_otro_hospital': forms.Select(attrs={'class': 'form-select'}),
            'tipo_matricula': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'tiene_acceso_sigehos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'otro_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'otro_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cuil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '11 dígitos sin guiones'}),
            'correo_gcba': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'usuario@buenosaires.gob.ar'}),
            'mail_personal': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 11 1234-5678'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Médico / Enfermero / Administrativo'}),
            'numero_matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'De no corresponder, colocar -'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especialidad acreditada'}),
            'servicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Clínica Médica / Cirugía'}),
            'dias_horarios': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Lunes a Viernes 8 a 14 hs'}),
            'area_trabajo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Sala 3 / Guardia / Mesón'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reemplaza la opción vacía en todos los desplegables por el texto en español
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ChoiceField):
                choices = list(field.choices)
                if choices and choices[0][0] == '':
                    choices[0] = ('', '- Seleccione una opción -')
                    field.choices = choices

    def clean_sitio_web(self):
        if self.cleaned_data.get('sitio_web'):
            raise forms.ValidationError("Acción no permitida.")
        return self.cleaned_data.get('sitio_web')

    def clean_cuil(self):
        cuil_raw = self.cleaned_data.get('cuil', '')
        cuil_limpio = re.sub(r'\D', '', cuil_raw)

        if len(cuil_limpio) != 11:
            raise forms.ValidationError("El CUIL debe contener exactamente 11 números sin guiones.")

        if Capacitado.objects.filter(cuil=cuil_limpio).exists():
            raise forms.ValidationError("Este número de CUIL ya se encuentra registrado.")

        return cuil_limpio

    def clean_mail_personal(self):
        return self.cleaned_data.get('mail_personal', '').strip().lower()

    def clean_correo_gcba(self):
        correo = self.cleaned_data.get('correo_gcba')
        return correo.strip().lower() if correo else None