import unittest
from todo import add_todo, remove_todo, todos

class TestTodo(unittest.TestCase):
    def setUp(self):
        global todos
        todos = []

    def test_add_todo(self):
        add_todo('Test todo')
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, 'Test todo')

    def test_remove_todo(self):
        add_todo('Test todo')
        add_todo('Another todo')
        remove_todo(1)
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, 'Another todo')

    def test_remove_nonexistent_todo(self):
        add_todo('Test todo')
        remove_todo(99)
        self.assertEqual(len(todos), 1)
        self.assertEqual(todos[0].title, 'Test todo')