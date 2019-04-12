import unittest
import os
import tempfile
from filecmp import cmp
import py_compile
from lib.vector_visualization import *

class FilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        cls.filter_path = os.path.join(cls.directory, "lib", "vector_visualization.py")
        cls.test_data_path= os.path.join(cls.directory, "tests", "test_data", "vector_visualization")
        cls.spacers = ["AAY", "HHHH", "GGS", "GPGPG", "HHAA", "AAL", "HH", "HHC", "HHH", "HHHD", "HHL", "HHHC"]

    def module_compiles(self):
        self.assertTrue(py_compile.compile(self.filter_path))

    def test_fasta_with_spacers(self):
        with tempfile.TemporaryDirectory() as output_dir:
            self.assertFalse(VectorVisualization(
                os.path.join(
                    self.test_data_path,
                    'input.spacers.fa'
                ),
                output_dir,
                self.spacers
            ).draw())
            self.assertTrue(os.path.exists(os.path.join(output_dir, 'vector.jpg')))
