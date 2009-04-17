import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
import messenger

class TestMessageSender(unittest.TestCase):
    def setUp(self):
        self.sender = messenger.Sender('adam')

    def test_send(self):
        self.assert_(self.sender.send('hello world'))

if __name__=='__main__':
    unittest.main()
