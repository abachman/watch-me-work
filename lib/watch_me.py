# Notifier example from tutorial
#
# See: http://trac.dbzteam.org/pyinotify/wiki/Tutorial for original example
#
from pyinotify import WatchManager, Notifier, ProcessEvent, \
    IN_DELETE, IN_CREATE, IN_MODIFY, WatchManagerError
import os

# Message sender
from messenger import NetworkSender as Sender
message_sender = Sender('adam')

ignore_prefixes = ('.gedit-save',)
ignore_suffixes = ('~',)

class Monitor(ProcessEvent):
    def send(self, k, e):
        notified_on = os.path.split(e)[1]
        for ig in ignore_prefixes:
            if notified_on.startswith(ig):
                return
        for ig in ignore_suffixes:
            if notified_on.endswith(ig):
                return
        message_sender.send("%s: %s" % (k, e))

    def process_IN_CREATE(self, event):
        self.send("Creating", event.pathname)

    def process_IN_DELETE(self, event):
        self.send("Removing", event.pathname)

    def process_IN_MODIFY(self, event):
        self.send("Modified", event.pathname)

def create_monitor(to_watch):
    "Create and start a new directory monitor."
    p = Monitor()
    wm = WatchManager()  # Watch Manager
    notifier = Notifier(wm, p, debug=True) # Notifier
    try: 
        wdd = wm.add_watch(to_watch, IN_DELETE | IN_CREATE | IN_MODIFY)
        notifier.loop()
    except WatchManagerError, err:
        print err, err.wmd


