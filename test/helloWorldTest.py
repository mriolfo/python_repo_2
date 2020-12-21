import unittest
# __init__.py tiene que tar
from code.helloWorld import HelloWorld

class HelloWorldTest(unittest.TestCase):
    def test_HelloWorld(self):
        greeter = HelloWorld()
        self.assertEqual(greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()