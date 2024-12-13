from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Task

@api_view(['GET'])
def home(request):
    """
    Renderiza la página de inicio.
    """
    return Response({"message": "Bienvenido al Microservicio"}, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    operation_description="Verifica el estado del microservicio",
    responses={200: openapi.Response(description="El microservicio está funcionando")}
)
@api_view(['GET'])
def health_check(request):
    """
    Verifica el estado del microservicio.
    """
    return Response({"status": "ok", "message": "Microservice is running!"}, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='post',
    operation_description="Crea una nueva tarea",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['title'],
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Título de la tarea'),
            'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Estado de la tarea', default=False),
        }
    ),
    responses={
        201: openapi.Response(description="Tarea creada exitosamente"),
        400: openapi.Response(description="Solicitud inválida"),
    }
)
@api_view(['POST'])
def create_task(request):
    """
    Crea una nueva tarea en la base de datos.
    """
    data = request.data
    if 'title' not in data or not data['title'].strip():
        return Response({'error': 'El campo "title" es obligatorio y no puede estar vacío'}, status=status.HTTP_400_BAD_REQUEST)
    task = Task.objects.create(
        title=data['title'],
        completed=data.get('completed', False)
    )
    return Response({'id': task.id, 'title': task.title, 'completed': task.completed}, status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    method='get',
    operation_description="Lista todas las tareas almacenadas",
    responses={200: openapi.Response(description="Lista de tareas")}
)
@api_view(['GET'])
def list_tasks(request):
    """
    Lista todas las tareas almacenadas.
    """
    tasks = Task.objects.all().values('id', 'title', 'completed')
    return Response(list(tasks), status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    operation_description="Obtiene los detalles de una tarea específica",
    responses={
        200: openapi.Response(description="Detalles de la tarea"),
        404: openapi.Response(description="Tarea no encontrada"),
    }
)
@api_view(['GET'])
def retrieve_task(request, task_id):
    """
    Obtiene los detalles de una tarea específica.
    """
    try:
        task = Task.objects.get(id=task_id)
        return Response({'id': task.id, 'title': task.title, 'completed': task.completed}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='put',
    operation_description="Actualiza una tarea existente",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Nuevo título de la tarea'),
            'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Nuevo estado de la tarea'),
        }
    ),
    responses={
        200: openapi.Response(description="Tarea actualizada exitosamente"),
        404: openapi.Response(description="Tarea no encontrada"),
        400: openapi.Response(description="Solicitud inválida"),
    }
)
@api_view(['PUT'])
def update_task(request, task_id):
    """
    Actualiza una tarea existente.
    """
    try:
        task = Task.objects.get(id=task_id)
        data = request.data
        if 'title' in data:
            if not data['title'].strip():
                return Response({'error': 'El campo "title" no puede estar vacío'}, status=status.HTTP_400_BAD_REQUEST)
            task.title = data['title']
        if 'completed' in data:
            task.completed = data['completed']
        task.save()
        return Response({'id': task.id, 'title': task.title, 'completed': task.completed}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='delete',
    operation_description="Elimina una tarea existente",
    responses={
        200: openapi.Response(description="Tarea eliminada correctamente"),
        404: openapi.Response(description="Tarea no encontrada"),
    }
)
@api_view(['DELETE'])
def delete_task(request, task_id):
    """
    Elimina una tarea existente.
    """
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return Response({'message': 'Tarea eliminada correctamente'}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Tarea no encontrada'}, status=status.HTTP_404_NOT_FOUND)