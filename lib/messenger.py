# This is where the action happens, Sender takes a name on 
# initialization and defines a `send` method that is called 
# and passed a message string on each monitored file system 
# event.
  
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

import liblo 

class NetworkSender(Sender):
    def __init__(self, name):
        Sender.__init__(self, name)
        try: 
            self.target = liblo.Address(1234)
        except liblo.AddressError, err:
            print str(err)
            raise
        print "Sending to %s (%s:%s)" % (self.target.get_url(),
                                         self.target.get_hostname(),
                                         self.target.get_port())
    def send(self, message):
        liblo.send(self.target, 
                "/notify", 
                self.name, 
                self.message(message))


