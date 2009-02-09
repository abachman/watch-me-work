import unittest
import sys
sys.path.append("../lib")
import watch_me

class TestNotifier(unittest.TestCase):
#    def setUp(self):
#        self.notifier = watch_me.Notifier()
    
    def test_true(self):
        self.assert_(True)

if __name__=='__main__':
    unittest.main()
