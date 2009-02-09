# Notifier example from tutorial
#
# See: http://trac.dbzteam.org/pyinotify/wiki/Tutorial for original example
#
from pyinotify import WatchManager, Notifier, ProcessEvent, \
    IN_DELETE, IN_CREATE, IN_MODIFY

# Watch directories
import walker, os
watch_dir = "/home/adam/workspace/psl-careercenter"
ignore = "log", ".svn", 'tiny_mce', 'plugins', 'tmp', 'content'
to_watch = walker.get_watch_directories(watch_dir, ignore)
print "Watching %i directories under %s" % (len(to_watch), watch_dir)

# Message sender
from messenger import Sender
message_sender = Sender('adam')

ignore_prefixes = ('.gedit-save',)
ignore_suffixes = ('~',)
class PTmp(ProcessEvent):
    def send(self, k, e):
        notified_on = os.split(e)[1]
        for ig in ignore_prefixes:
            if notified_on.starts_with(ig):
                return
        for ig in ignore_suffixes:
            if notified_on.ends_with(ig):
                return
        message_sender.send("%s: %s" % (k, e))

    def process_IN_CREATE(self, event):
        self.send("Creating", event.pathname)

    def process_IN_DELETE(self, event):
        self.send("Removing", event.pathname)

    def process_IN_MODIFY(self, event):
        self.send("Modified", event.pathname)

p = PTmp()
wm = WatchManager()  # Watch Manager
notifier = Notifier(wm, p) # Notifier
wdd = wm.add_watch(to_watch, IN_DELETE | IN_CREATE | IN_MODIFY)

notifier.loop()
