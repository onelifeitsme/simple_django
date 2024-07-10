from django.test import TestCase


class FirstTest(TestCase):
    def test_first(self):
        a = 0
        b = 0
        self.assertEqual(a, b)