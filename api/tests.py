from django.test import TestCase
from django.urls import reverse
from .models import Task

class HealthCheckTestCase(TestCase):
    def test_health_check(self):
        """
        Prueba para verificar el estado del microservicio.
        """
        response = self.client.get(reverse('health_check'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok", "message": "Microservice is running!"})

class TaskTestCase(TestCase):
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        self.task_data = {"title": "Prueba de tarea", "completed": False}
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        """
        Prueba para crear una nueva tarea.
        """
        response = self.client.post(
            reverse('create_task'),
            data={"title": "Nueva tarea", "completed": True},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], "Nueva tarea")
        self.assertEqual(response.json()['completed'], True)

    def test_list_tasks(self):
        """
        Prueba para listar todas las tareas.
        """
        response = self.client.get(reverse('list_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['title'], self.task_data['title'])

    def test_retrieve_task(self):
        """
        Prueba para obtener los detalles de una tarea específica.
        """
        response = self.client.get(reverse('retrieve_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], self.task_data['title'])

    def test_update_task(self):
        """
        Prueba para actualizar una tarea existente.
        """
        response = self.client.put(
            reverse('update_task', args=[self.task.id]),
            data={"title": "Tarea actualizada", "completed": True},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], "Tarea actualizada")
        self.assertEqual(response.json()['completed'], True)

    def test_delete_task(self):
        """
        Prueba para eliminar una tarea existente.
        """
        response = self.client.delete(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Tarea eliminada correctamente")
        # Verificar que la tarea ya no existe
        response = self.client.get(reverse('retrieve_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 404)

    def test_create_task_invalid(self):
        """
        Prueba para manejar una solicitud inválida al crear una tarea.
        """
        response = self.client.post(
            reverse('create_task'),
            data={"title": ""},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['error'], 'El campo "title" es obligatorio y no puede estar vacío')

    def test_retrieve_nonexistent_task(self):
        """
        Prueba para obtener una tarea inexistente.
        """
        response = self.client.get(reverse('retrieve_task', args=[999]))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], "Tarea no encontrada")

    def test_update_nonexistent_task(self):
        """
        Prueba para actualizar una tarea inexistente.
        """
        response = self.client.put(
            reverse('update_task', args=[999]),
            data={"title": "Intento fallido", "completed": True},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], "Tarea no encontrada")

    def test_delete_nonexistent_task(self):
        """
        Prueba para eliminar una tarea inexistente.
        """
        response = self.client.delete(reverse('delete_task', args=[999]))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], "Tarea no encontrada")