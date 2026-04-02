import unittest

from basic import SuperHero

class TestSupreHero(unittest.TestCase):
    def setUp(self):
        self.superHero = SuperHero(name="Superman", strength_level= 50)
        
    def test_stringify(self):
        self.assertEqual(str(self.superHero), "Superman")
        
    def test_is_stronger_than_other_superhere(self):
        other_superHero = SuperHero(name="Batman", strength_level=35)
        
        self.assertTrue(self.superHero.is_stronger_than(other_superHero))
        self.assertFalse(other_superHero.is_stronger_than(self.superHero))