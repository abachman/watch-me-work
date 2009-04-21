#!/usr/bin/env python

import sys, os; 
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))
import watch_me
import walker
from config import config

## TEST MODE {{{
import create_directories
create_directories.create_tmp_directories()
## }}}

# Watch directories
if len(sys.argv) == 2:
    watch_dir = os.path.abspath(sys.argv[1])
    username = config['username']
elif len(sys.argv) == 3:
    watch_dir = os.path.abspath(sys.argv[1])
    username = os.path.abspath(sys.argv[1])
else:
    watch_dir = 'tmp/'
    username = config['username']

to_watch = walker.get_watch_directories(watch_dir)
print "Watching %i directories under %s on behalf of %s" % \
    (len(to_watch), watch_dir, username)

try:
    watch_me.create_monitor(to_watch, username)
finally:
    create_directories.remove_tmp_directories()
    

