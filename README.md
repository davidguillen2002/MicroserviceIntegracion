# Microservicio Django - Práctica de Microservicios y Contenedores

   ## Descripción
   Este microservicio básico verifica su estado mediante el endpoint `/api/health/`.

   ## Requisitos
   - Docker y Docker Compose instalados.
   - Python 3.10 (solo para desarrollo local).

   ## Instrucciones para ejecutar
   1. Construir la imagen:
      ```bash
      docker-compose build
      ```
   2. Iniciar el contenedor:
      ```bash
      docker-compose up
      ```
   3. Acceder a `http://127.0.0.1:8000/api/health/` para verificar el estado.