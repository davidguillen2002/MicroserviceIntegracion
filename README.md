# Microservicio Django - Práctica de Microservicios y Contenedores

## Descripción
Este microservicio implementa un CRUD completo para gestionar tareas, además de incluir un endpoint para verificar el estado del servicio. La documentación interactiva se genera automáticamente utilizando Swagger.

### Funcionalidades principales
- **Verificar el estado del servicio:** Endpoint `/api/health/`.
- **CRUD de tareas:**
  - Crear tarea: `POST /api/tasks/`
  - Listar tareas: `GET /api/tasks/list/`
  - Obtener tarea específica: `GET /api/tasks/<task_id>/`
  - Actualizar tarea: `PUT /api/tasks/<task_id>/update/`
  - Eliminar tarea: `DELETE /api/tasks/<task_id>/delete/`
- **Documentación interactiva:** Acceso a Swagger en `/swagger/`.

---

## Requisitos
- **Docker y Docker Compose instalados.**
- **Python 3.10 (solo si deseas ejecutar el microservicio de forma local, sin Docker).**

---

## Instrucciones para ejecutar con Docker
1. **Clonar el repositorio (si aplica):**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd MicroserviceIntegracion
   ```

2. **Construir la imagen:**
   ```bash
   docker-compose build
   ```

3. **Iniciar los contenedores:**
   ```bash
   docker-compose up
   ```

4. **Verificar el estado del servicio:**
   Accede al endpoint de salud en `http://127.0.0.1:8000/api/health/`.

5. **Explorar la documentación interactiva:**
   Abre Swagger en `http://127.0.0.1:8000/swagger/`.

---

## Ejecución local (sin Docker)
Si prefieres ejecutar el microservicio directamente en tu entorno local:

1. **Instalar dependencias:**
   Asegúrate de tener un entorno virtual activado y ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar la base de datos:**
   Asegúrate de que el archivo `settings.py` tiene configurada una base de datos local válida (por ejemplo, PostgreSQL).

3. **Aplicar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Iniciar el servidor:**
   ```bash
   python manage.py runserver
   ```

5. **Probar los endpoints:**
   - Estado del servicio: `http://127.0.0.1:8000/api/health/`
   - Documentación Swagger: `http://127.0.0.1:8000/swagger/`

---

## Pruebas automatizadas
El microservicio incluye pruebas automatizadas para validar el comportamiento de los endpoints:

1. **Ejecutar las pruebas:**
   ```bash
   python manage.py test
   ```

2. **Resultados esperados:**
   Si todo está configurado correctamente, deberías ver algo como:
   ```
   Ran 10 tests in X.XXXs

   OK
   ```

---

## Tecnologías utilizadas
- **Django 5.1.4**
- **Django REST Framework**
- **Swagger (drf-yasg)**
- **PostgreSQL (base de datos)**
- **Docker y Docker Compose**

---

## Autores
David Guillén, Johann Ordoñez, Gustavo Guevara y Johan Carrasco.
