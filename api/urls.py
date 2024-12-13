from django.urls import path
from .views import home, health_check, create_task, list_tasks, retrieve_task, update_task, delete_task
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Microservice API",
        default_version='v1',
        description="Documentación de la API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Definición de las rutas
urlpatterns = [
    path('', home, name='home'),
    path('health/', health_check, name='health_check'),
    path('tasks/', create_task, name='create_task'),  # Crear tarea (POST)
    path('tasks/list/', list_tasks, name='list_tasks'),  # Listar tareas (GET)
    path('tasks/<int:task_id>/', retrieve_task, name='retrieve_task'),  # Obtener tarea específica (GET)
    path('tasks/<int:task_id>/update/', update_task, name='update_task'),  # Actualizar tarea (PUT)
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),  # Eliminar tarea (DELETE)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]