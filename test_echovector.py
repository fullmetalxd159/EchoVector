# test_echovector.py
"""
Tests for EchoVector module.
"""

import unittest
from echovector import EchoVector

class TestEchoVector(unittest.TestCase):
    """Test cases for EchoVector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EchoVector()
        self.assertIsInstance(instance, EchoVector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EchoVector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
