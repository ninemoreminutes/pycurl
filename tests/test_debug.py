# $Id: test_debug.py,v 1.2 2002/04/15 12:02:59 kjetilja Exp $

import pycurl

def test(t, b):
    print "debug(%d): %s" % (t, b)

c = pycurl.init()
c.setopt(pycurl.URL, 'http://curl.haxx.se/')
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.DEBUGFUNCTION, test)
c.perform()
c.cleanup()
