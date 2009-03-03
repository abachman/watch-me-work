import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import watch_me

class TestNotifier(unittest.TestCase):
    def test_true(self):
        self.assert_(True)

if __name__=='__main__':
    unittest.main()
