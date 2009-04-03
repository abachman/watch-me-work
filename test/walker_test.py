import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import walker

class TestWalker(unittest.TestCase):
    def setUp(self):
        pass 
   
    def test_send(self):
        self.assert_( true )

if __name__=='__main__':
    unittest.main()
