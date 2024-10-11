import unittest
from ajedrezoo import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ob = metapieza(10,2,"c") # se ejecuta el constructor de metapieza
        self.assertEqual(0,0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
