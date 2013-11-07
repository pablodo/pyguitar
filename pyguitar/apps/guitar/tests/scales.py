from django.test import SimpleTestCase

from pyguitar.apps.guitar.scales import make_scale
from pyguitar.apps.guitar.scales import ScaleNotFoundError


class ScalesTest(SimpleTestCase):

    def test_make_pentatonic(self):
        expected = ['a', 'c', 'd', 'e', 'g', 'a']
        self.assertEquals(expected, make_scale('a', 'pentatonic'))

    def test_make_minor(self):
        expected = ['d', 'e', 'f', 'g', 'a', 'a#', 'c', 'd']
        self.assertEquals(expected, make_scale('d', 'minor'))

    def test_make_major(self):
        expected = ['g', 'a', 'b', 'c', 'd', 'e', 'f#', 'g']
        self.assertEquals(expected, make_scale('g', 'major'))

    def test_make_armonic_minor(self):
        expected = ['c', 'd', 'd#', 'f', 'g', 'g#', 'b', 'c']
        self.assertEquals(expected, make_scale('c', 'armonic_minor'))

    def test_non_existent_mode(self):
        self.assertRaises(ScaleNotFoundError, make_scale, 'a', 'wrong')

