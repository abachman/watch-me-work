#!/usr/bin/env python

import sys, os; 
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))
import watch_me
import walker

## TEST MODE {{{
import create_directories
create_directories.create_tmp_directories()
## }}}

# Watch directories
watch_dir = len(sys.argv) == 2 and os.path.abspath(sys.argv[1]) or 'tmp/'
to_watch = walker.get_watch_directories(watch_dir)
print "Watching %i directories under %s" % (len(to_watch), watch_dir)

try:
    watch_me.create_monitor(to_watch)
finally:
    create_directories.remove_tmp_directories()
    

