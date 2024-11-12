# tests/test_task_manager.py
import unittest
from src.logico import TaskManager, Task

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Estudiar", "Revisar capítulos 1-3")
        self.assertEqual(task.title, "Estudiar")
        self.assertEqual(task.description, "Revisar capítulos 1-3")
        self.assertFalse(task.completed)

    def test_list_tasks(self):
        self.manager.add_task("Estudiar")
        self.manager.add_task("Hacer ejercicio")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Estudiar")
        self.assertEqual(tasks[1].title, "Hacer ejercicio")

    def test_delete_task(self):
        self.manager.add_task("Estudiar")
        self.manager.add_task("Hacer ejercicio")
        self.manager.delete_task("Estudiar")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Hacer ejercicio")

    def test_complete_task(self):
        self.manager.add_task("Estudiar")
        task = self.manager.complete_task("Estudiar")
        self.assertTrue(task.completed)

    def test_complete_nonexistent_task(self):
        task = self.manager.complete_task("Inexistente")
        self.assertIsNone(task)


if __name__ == "__main__":
    unittest.main()
