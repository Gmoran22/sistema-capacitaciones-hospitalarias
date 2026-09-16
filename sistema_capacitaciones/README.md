# Sistema de Gestión de Capacitaciones Hospitalarias

Aplicación web desarrollada con Django y MySQL para optimizar la toma de asistencia y registro del personal sanitario en capacitaciones hospitalarias mediante código QR, eliminando la carga manual diferida y permitiendo la exportación directa a nóminas oficiales en Excel.

## Tecnologías Utilizadas

* **Backend:** Python / Django
* **Base de Datos:** MySQL
* **Frontend:** Bootstrap 5 (Responsive / Mobile First)
* **Gestión de Datos:** OpenPyXL (Reportes Excel automatizados)
* **Configuración:** Python-Decouple (.env)

## Requisitos Previos

* Python 3.10 o superior
* Servidor MySQL Server activo

## Instalación y Puesta en Marcha

1. **Clonar el repositorio:**
   \`\`\`bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   cd sistema_capacitaciones
   \`\`\`

2. **Crear y activar el entorno virtual:**
   \`\`\`powershell
   python -m venv venv
   .\venv\Scripts\activate
   \`\`\`

3. **Instalar dependencias:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Configurar variables de entorno:**
   Copiar el archivo `.env.example` a `.env` y completar con las credenciales de la base de datos MySQL local:
   \`\`\`bash
   cp .env.example .env
   \`\`\`

5. **Aplicar migraciones:**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

6. **Crear usuario administrador:**
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

7. **Ejecutar el servidor:**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

* **Formulario público:** `http://127.0.0.1:8000/`
* **Panel de Administración:** `http://127.0.0.1:8000/admin/`
* **Exportación de Excel:** `http://127.0.0.1:8000/exportar-excel/`