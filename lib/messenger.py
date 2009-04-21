# This is where the action happens, Sender takes a name on 
# initialization and defines a `send` method that is called 
# and passed a message string on each monitored file system 
# event.

from config import config 
import liblo 

class Sender(object):
    from time import time 
    def __init__(self, name):
        self.name = name
    def message(self, message):
        return "[%s] %s" % (self.time(), message)

    # override this
    def send(self, message):
        print self.message(message)
        return True


class NetworkSender(Sender):
    def __init__(self, name):
        Sender.__init__(self, name)
        try: 
            self.target = liblo.Address(*config['target'])
        except liblo.AddressError, err:
            print str(err)
            raise
        targ = self.target
        print "Sending to %s (%s:%s)" % \
            (targ.get_url(), targ.get_hostname(), targ.get_port())
        self.register()

    def register(self):
        liblo.send(self.target,
           "/register",
           self.name)

    def send(self, message):
        print self.message(message)
        liblo.send(self.target, 
            "/notify", 
            self.name, 
            self.message(message))



