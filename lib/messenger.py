# This is where the action happens, Sender takes a name on 
# initialization and defines a `send` method that is called 
# and passed a message string on each monitored file system 
# event.

class Sender(object):
    def __init__(self, name):
        self.name = name
    def message(self, name, message):
        return "[%s] %s" % (self.name, message)

    def send(self, message):
        print self.message(self.name, message)
        return True

class NetworkSender(Sender):
    def send(self, msg):
        print self.message(self.name, msg + " (sent from " + self.__class__.__name__ + ")")
