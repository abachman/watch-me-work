#!/usr/bin/env python

import liblo, sys

# create server, listening on port 1234
try:
    server = liblo.Server(1234)
except liblo.ServerError, err:
    print str(err)
    sys.exit()

def notify_callback(path, args):
    name, message = args
    print "{%s} %s" % (name, message)

def fallback(path, args, types, src):
    print "got unknown message '%s' from '%s'" % (path, src.get_url())
    for a, t in zip(args, types):
        print "argument of type '%s': %s" % (t, a)

print 'registering methods...'
# register method taking an int and a float
server.add_method("/notify", 'ss', notify_callback)

# register a fallback for unhandled messages
server.add_method(None, None, fallback)

print 'listening on %s' % (server.get_url())

# loop and dispatch messages every 100ms
while True:
    server.recv(100)

