import unittest
from app.main import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_simple(self):
        expected_output = "Hello World!"
        result = hello_world()
        self.assertEqual(result, expected_output)

