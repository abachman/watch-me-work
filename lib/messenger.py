class Sender:
    def __init__(self, name):
        self.name = name
    def send(self, message):
        print "[%s] %s" % (self.name, message)
        return True
