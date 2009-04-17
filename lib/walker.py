import os

def get_watch_directories(root, ignore=None):
    if not ignore:
        ignore = []
    to_watch = []
    for r, d, f in os.walk(root):
        to_watch.append(r)
        for ig in ignore:
            if ig in d: d.remove(ig)
    return to_watch

if __name__=='__main__':
    watch_dir = "/home/adam/workspace/psl-careercenter"
    ignore = "log", ".svn", 'tiny_mce', 'plugins', 'tmp', 'content'
    to_watch = get_watch_directories(watch_dir, ignore)
    print '\n'.join(to_watch)
    print "Watching", len(to_watch), "directories"
