# $Id: test_debug.py,v 1.1 2002/04/15 11:05:59 kjetilja Exp $

import pycurl

def test(**args):
    print args

c = pycurl.init()
c.setopt(pycurl.URL, 'http://curl.haxx.se/')
c.setopt(pycurl.VERBOSE, 1)
c.setopt(pycurl.DEBUGFUNCTION, test)
c.perform()
c.cleanup()
