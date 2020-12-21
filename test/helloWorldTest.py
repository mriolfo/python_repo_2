import unittest
from helloWorld.py import HelloWorld

class HelloWorldTest(unittest.TestCase):
    def test_HelloWorld(self):
        greeter = HelloWorld()
        self.assertEqual(greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()