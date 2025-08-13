# Improvement & Results API

API desarrollada con **Django REST Framework** que permite:

* Realizar una carga inicial de datos desde una API externa.
* Ejecutar procesos de mejora (*sweeps*) hasta eliminar registros con categoría `bad`.
* Consultar, crear, editar y eliminar resultados.


## Características principales

* Arquitectura modular con separación en **Services**, **Repositories** y **Views**.
* Modelos claros y reutilizables.
* Endpoints RESTful documentados.


## Requisitos previos

* Python 3.10 o superior
* pip
* virtualenv (opcional, pero recomendado)
* PostgreSQL o SQLite (para desarrollo rápido)

## Instalación

1. Clonar el repositorio:
   `https://github.com/Nico453/Prueba_Tecnica.git && cd Prueba_Tecnica`
2. Crear entorno virtual:

   * Linux/Mac: `python -m venv venv && source venv/bin/activate`
   * Windows: `python -m venv venv && venv\\Scripts\\activate`
3. Instalar dependencias:
   `pip install -r requirements.txt`
4. Configurar variables de entorno creando un archivo **.env** en la raíz del proyecto con:

   ```
   DEBUG=True
   SECRET_KEY=change-me
   
   DB_NAME=nombre_de_tu_base
   DB_USER=usuario_de_tu_base
   DB_PASSWORD=contraseña_de_tu_base
   DB_HOST=127.0.0.1
   DB_PORT=5432
   
   API_USER_ID=DU54D2
   API_BASE_URL=https://4advance.co/testapi/get.php
   API_TIMEOUT=5
   API_MAX_RETRIES=3
   API_BACKOFF=0.5
   ```

  
5. Migrar la base de datos y ejecutar el servidor:
   `python manage.py migrate && python manage.py runserver`

## Pruebas de la API

### 1. Primera ejecución (carga inicial)

**POST** `/api/results/load_initial/`
Respuesta esperada:

```
{
  "loaded": 100,
  "bad": 64,
  "medium": 22,
  "good": 14,
  "reset_performed": true
}
```

### 2. Barrido (sweeps)

**POST** `/api/results/sweep/`
Respuesta esperada:

```
{
  "sweeps": 13,
  "improvement_calls": 155
}
```

### 3. Consultar resultados

**GET** `/api/results/`
Devuelve la lista de todos los resultados.

**GET** `/api/results/{id}/`
Devuelve el detalle de un resultado específico.

## Estructura de endpoints

| Método    | Endpoint                    | Descripción                                               |
| --------- | --------------------------- | --------------------------------------------------------- |
| GET       | /api/results/               | Lista todos los resultados                                |
| POST      | /api/results/               | Crea un nuevo resultado                                   |
| GET       | /api/results/{id}/          | Obtiene un resultado específico                           |
| PUT/PATCH | /api/results/{id}/          | Edita un resultado existente                              |
| DELETE    | /api/results/{id}/          | Elimina un resultado                                      |
| POST      | /api/results/load\_initial/ | Carga inicial de *n* registros desde API externa          |
| POST      | /api/results/sweep/         | Ejecuta barridos hasta eliminar todos los registros `bad` |

