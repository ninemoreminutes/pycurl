#! /usr/bin/env python
# vi:ts=4:et
# $Id: test_debug.py,v 1.5 2002/08/29 14:39:20 mfx Exp $

import pycurl

def test(t, b):
    print "debug(%d): %s" % (t, b)

c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://curl.haxx.se/')
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.DEBUGFUNCTION, test)
c.perform()
c.close()
