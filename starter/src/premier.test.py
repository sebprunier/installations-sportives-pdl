import unittest
from premier import estPremier

class TestEstPremier(unittest.TestCase):

  def test_estPremier(self):
      self.assertFalse(estPremier(-1))
      self.assertFalse(estPremier(0))
      self.assertFalse(estPremier(1))
      self.assertTrue(estPremier(2))
      self.assertFalse(estPremier(4))
      self.assertTrue(estPremier(11))
      self.assertRaises(ValueError, lambda: estPremier(1.3))

if __name__ == '__main__':
    unittest.main()
