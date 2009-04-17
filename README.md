# watch-me-work

an office based sound installation for Ubuntu linux.

To run, open three command lines. In the first:

    $ ./server.sh

In the second: 

    $ python run.py

In the third:

    $ echo '' >> tmp/asdf.txt

You should see text getting spit out of the first console (or wherever you have the server running).

### Requirements:

[pyliblo][pyliblo], a python wrapper for the liblo OSC library.

### Status

**2009-04-15** Added config file at lib/config.py, you can use that to change some basic settings on the client and server sides.

**2009-04-02** Can send signals across local connection between file watcher (client) and notification server. 

### TODO

* include [boodler soundscape toolkit][boodler].
* experiment with larger data chunks over the wire (e.g., fstat calls on modified files, more metadata)
* experiment with interaction across network connections, VMs perhaps?
* implement /register function on server. Expand function of server in general.
* find a way to include an OSC library, perhaps explore [simpleosc][sosc] in more depth.
* experiment with non-python servers (processing.org, chuck, pd, ?)

[pyliblo]: http://das.nasophon.de/pyliblo/
[boodler]: http://boodler.org/
[sosc]: http://www.ixi-software.net/content/body_backyard_osc.html
