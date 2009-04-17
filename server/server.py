#!/usr/bin/env python

import liblo
from liblo import *

import sys, os
libdir = os.path.join(os.path.dirname(__file__), "..", "lib")
sys.path.append(libdir)
from config import config

class Processor:
    def __init__(self):
        self.data = {}
    def register(self, name):
        self.data[name] = []
        print "Hey, %s just joined the party!" % (name)
    def process(self, name, message):
        if not name in self.data:
            self.register(name)
        self.data[name].append(message)
        print "{%s} %s" % (name, message)


class WatchServer(liblo.ServerThread):
    def __init__(self):
        # Start server on default port.
        ServerThread.__init__(self, config['port'])
        self.processor = Processor()

    @make_method('/notify', 'ss')
    def notify_callback(self, path, args):
        name, message = args
        self.processor.process(name, message)

    @make_method('/register', 's')
    def registration_callback(self, path, args):
        name = args[0]
        self.processor.register(name)

    @make_method(None, None)
    def fallback(self, path, args, types, src):
        print "got unknown message '%s' from '%s'" % (path, src.get_url())
        for a, t in zip(args, types):
            print "argument of type '%s': %s" % (t, a)

try: 
    server = WatchServer()
except ServerError, err:
    print str(err)
    sys.exit()

print 'listening on %s' % (server.get_url())

server.start()

import time
try:
    # let the server thread run for an hour
    time.sleep(3600)
except KeyboardInterrupt:
    pass
print server.processor.data
