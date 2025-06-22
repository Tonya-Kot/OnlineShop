import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_output(self):
        # Можно проверить вывод или логи, здесь просто пример
        self.assertIsNone(main())

if __name__ == '__main__':
    unittest.main()
