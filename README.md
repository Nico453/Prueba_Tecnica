# **Improvement & Results API**

API en **Django REST Framework** que permite:
- Realizar carga inicial de datos desde una API externa.
- Ejecutar procesos de mejora ("sweeps") hasta eliminar registros con categoría `bad`.
- Consultar, crear, editar y eliminar resultados.
- Proveer endpoints listos para integrar con un frontend.

---

## **Características principales**
- Arquitectura modular con separación de **Services**, **Repositories** y **Views**.
- Modelos claros y reutilizables.
- Endpoints RESTful documentados.
- Tests unitarios con `pytest` y `pytest-django`.
- Configuración para permitir integración con frontends externos mediante **CORS**.

---

## **Requisitos previos**
- Python 3.10+
- pip
- virtualenv (opcional pero recomendado)
- PostgreSQL o SQLite (para desarrollo rápido)

---

## **Instalación**
1. **Clonar el repositorio**

git clone https://github.com/usuario/mi-proyecto.git
cd mi-proyecto
  
2. **Crear entorno virtual**
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. **Instalar dependencias**
pip install -r requirements.txt


4. **Configurar variables de entorno**
# ========================
# Django Configuration
# ========================
# Cambia DEBUG a False en producción
DEBUG=True
SECRET_KEY=change-me

# ========================
# Database Configuration
# ========================
# Reemplaza estos valores por los de tu propia base de datos
DB_NAME=nombre_de_tu_base
DB_USER=usuario_de_tu_base
DB_PASSWORD=contraseña_de_tu_base
DB_HOST=127.0.0.1
DB_PORT=5432

# ========================
# External API Configuration
# ========================
API_USER_ID=DU54D2
API_BASE_URL=https://4advance.co/testapi/get.php
API_TIMEOUT=5
API_MAX_RETRIES=3
API_BACKOFF=0.5


4. **Migrar BD y ejecutar**
python manage.py migrate
python manage.py runserver



