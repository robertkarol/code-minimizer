import unittest
import importlib

class SampleTest(unittest.TestCase):

    def test_upper(self):
        sample = importlib.import_module('sample')
        importlib.reload(sample)
        val = sample.get_number_five()
        self.assertEqual(5, val)
