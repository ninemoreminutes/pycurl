# $Id: basicfirst.py,v 1.3 2002/03/08 11:06:38 kjetilja Exp $

import sys
import pycurl

url = 'http://curl.haxx.se/dev/'
contents = ''

def body_callback(buf):
    global contents
    contents = contents + buf
    return len(buf)

print 'Testing', pycurl.version

c = pycurl.init()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.WRITEFUNCTION, body_callback)
c.setopt(pycurl.HTTPHEADER, ["I-am-a-silly-programmer: yes indeed you are",
                             "User-Agent: Python interface for libcURL"])
c.perform()
c.cleanup()

print contents
