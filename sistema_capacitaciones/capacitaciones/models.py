from django.db import models

class Capacitado(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('MEDICO', 'Médico/a'),
        ('NO_MEDICO', 'Profesional de salud No médico'),
        ('ADMINISTRATIVO', 'Administrativo/a'),
        ('JEFE_ADMINISTRATIVO', 'Jefe administrativo'),
    ]

    PERMISOS_CHOICES = [
        ('HISINT_MEDICO', 'HISINT - PROFESIONAL MEDICO'),
        ('HISINT_NO_MEDICO', 'HISINT PROFESIONAL NO MEDICO'),
        ('GDEE_JEFE', 'GDEE-JEFE MESON o DEPARTAMENTO INTGRAL'),
        ('GDEE_ADMIN', 'GDEE-ADMINISTRATIVO MESON INTGRAL'),
    ]

    HOSPITALES_CHOICES = [
        ('No', 'No'),
        ('Hospital General de Agudos Dr. T. Álvarez', 'Hospital General de Agudos Dr. T. Álvarez'),
        ('Hospital General de Agudos Dr. C. Argerich', 'Hospital General de Agudos Dr. C. Argerich'),
        ('Hospital General de Agudos Dr. C. Durand', 'Hospital General de Agudos Dr. C. Durand'),
        ('Hospital General de Agudos Dr. J. A. Fernández', 'Hospital General de Agudos Dr. J. A. Fernández'),
        ('Hospital General de Agudos Dra. Cecilia Grierson', 'Hospital General de Agudos Dra. Cecilia Grierson'),
        ('Hospital General de Agudos J. M. Penna', 'Hospital General de Agudos J. M. Penna'),
        ('Hospital General de Agudos P. Piñero', 'Hospital General de Agudos P. Piñero'),
        ('Hospital General de Agudos Dr. I. Pirovano', 'Hospital General de Agudos Dr. I. Pirovano'),
        ('Hospital General de Agudos J. M. Ramos Mejía', 'Hospital General de Agudos J. M. Ramos Mejía'),
        ('Hospital General de Agudos B. Rivadavia', 'Hospital General de Agudos B. Rivadavia'),
        ('Hospital General de Agudos Donación F. Santojanni', 'Hospital General de Agudos Donación F. Santojanni'),
        ('Hospital General de Agudos Dr. E. Tornú', 'Hospital General de Agudos Dr. E. Tornú'),
        ('Hospital General de Agudos D. Vélez Sarsfield', 'Hospital General de Agudos D. Vélez Sarsfield'),
        ('Hospital General de Agudos A. Zubizarreta', 'Hospital General de Agudos A. Zubizarreta'),
        ('Hospital General de Niños Pedro de Elizalde', 'Hospital General de Niños Pedro de Elizalde'),
        ('Hospital General de Niños Ricardo Gutiérrez', 'Hospital General de Niños Ricardo Gutiérrez'),
        ('Hospital de Emergencias Psiquiátricas Torcuato de Alvear', 'Hospital de Emergencias Psiquiátricas Torcuato de Alvear'),
        ('Hospital de Salud Mental Braulio Moyano', 'Hospital de Salud Mental Braulio Moyano'),
        ('Hospital de Salud Mental J. T. Borda', 'Hospital de Salud Mental J. T. Borda'),
        ('Hospital Infanto Juvenil C. Tobar García', 'Hospital Infanto Juvenil C. Tobar García'),
        ('Hospital de Odontología José Dueñas', 'Hospital de Odontología José Dueñas'),
        ('Hospital de Odontología Dr. Ramón Carrillo (ex nacional)', 'Hospital de Odontología Dr. Ramón Carrillo (ex nacional)'),
        ('Hospital de Odontología Infantil Don Benito Quinquela Martín', 'Hospital de Odontología Infantil Don Benito Quinquela Martín'),
        ('Hospital de Oftalmología Santa Lucía', 'Hospital de Oftalmología Santa Lucía'),
        ('Hospital Oftalmológico Dr. Pedro Lagleyze', 'Hospital Oftalmológico Dr. Pedro Lagleyze'),
        ('Hospital de Gastroenterología B. Udaondo', 'Hospital de Gastroenterología B. Udaondo'),
        ('Hospital Municipal de Oncología María Curie', 'Hospital Municipal de Oncología María Curie'),
        ('Hospital de Rehabilitación Respiratoria M. Ferrer', 'Hospital de Rehabilitación Respiratoria M. Ferrer'),
        ('Hospital de Infecciosas F. Muñiz', 'Hospital de Infecciosas F. Muñiz'),
        ('Instituto de Zoonosis L. Pasteur', 'Instituto de Zoonosis L. Pasteur'),
        ('Instituto de Rehabilitación Psicofísica ( I.R.E.P. )', 'Instituto de Rehabilitación Psicofísica ( I.R.E.P. )'),
        ('Hospital de Quemados Dr. Arturo Umberto Illia', 'Hospital de Quemados Dr. Arturo Umberto Illia'),
        ('Hospital de Rehabilitación M. Rocca', 'Hospital de Rehabilitación M. Rocca'),
        ('Hospital Materno Infantil R. Sardá', 'Hospital Materno Infantil R. Sardá'),
    ]

    TIPO_MATRICULA_CHOICES = [
        ('NACIONAL', 'Matrícula Nacional (MN) [Prioritaria]'),
        ('PROVINCIAL', 'Matrícula Provincial (MP)'),
        ('OTRA', 'Otra Matrícula'),
        ('NO_CORRESPONDE', 'No corresponde (-)'),
    ]

    CATEGORIA_CHOICES = [
        ('PLANTA_PERMANENTE', 'Planta permanente'),
        ('RESIDENTE', 'Residente'),
        ('CONTRATO', 'Contrato'),
    ]

    # --- CAMPOS CLAVE (7 OBLIGATORIOS) ---
    cuil = models.CharField(max_length=11, unique=True, verbose_name="CUIL")
    apellido = models.CharField(max_length=100, verbose_name="Primer Apellido")
    nombre = models.CharField(max_length=100, verbose_name="Primer Nombre")
    mail_personal = models.EmailField(verbose_name="Mail Personal")
    telefono = models.CharField(max_length=50, verbose_name="Teléfono Personal")
    permisos_solicitar = models.CharField(max_length=40, choices=PERMISOS_CHOICES, verbose_name="Permisos a solicitar")
    servicio = models.CharField(max_length=150, verbose_name="Servicio")

    # --- CAMPOS SECUNDARIOS (OPCIONALES: blank=True, null=True) ---
    tipo_usuario = models.CharField(max_length=30, choices=TIPO_USUARIO_CHOICES, blank=True, null=True, verbose_name="Tipo de Usuario")
    trabaja_otro_hospital = models.CharField(max_length=150, choices=HOSPITALES_CHOICES, default='No', blank=True, null=True, verbose_name="Trabaja en otro hospital? (Cuál?)")
    tiene_acceso_sigehos = models.BooleanField(default=False, verbose_name="¿Tiene acceso a SIGEHOS?")
    otro_apellido = models.CharField(max_length=100, blank=True, null=True, verbose_name="Otro Apellido")
    otro_nombre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Otro Nombre")
    correo_gcba = models.EmailField(blank=True, null=True, verbose_name="Correo GCBA")
    profesion = models.CharField(max_length=120, blank=True, null=True, verbose_name="Profesión")
    tipo_matricula = models.CharField(max_length=20, choices=TIPO_MATRICULA_CHOICES, blank=True, null=True, verbose_name="Tipo de Matrícula")
    numero_matricula = models.CharField(max_length=50, blank=True, null=True, default='-', verbose_name="Nº de Matrícula")
    especialidad = models.CharField(max_length=150, blank=True, null=True, verbose_name="Especialidad Acreditada")
    dias_horarios = models.CharField(max_length=150, blank=True, null=True, verbose_name="Días y Horarios")
    area_trabajo = models.CharField(max_length=150, blank=True, null=True, verbose_name="Área de trabajo (Sala)")
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, blank=True, null=True, verbose_name="Categoría")

    # Auditoría interna
    material_enviado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'capacitados'
        verbose_name = 'Personal Capacitado'
        verbose_name_plural = 'Personal Capacitado'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.cuil})"