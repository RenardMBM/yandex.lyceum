import unittest
from yandex_testing_lesson import reverse


class TestFunctionReverse(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse(''), '')

    def test_one_symbol(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrome(self):
        self.assertEqual(reverse('foxof'), 'foxof')

    def test_regular_string(self):
        self.assertEqual(reverse('drofxO'), 'Oxford')

    def test_wrong_type_int(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_wrong_type_list(self):
        with self.assertRaises(TypeError):
            reverse(['d', 'r', 'o', 'f', 'x', 'O'])


if __name__ == '__main__':
    unittest.main()
