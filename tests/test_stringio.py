# $Id: test_stringio.py,v 1.2 2002/03/08 11:07:57 kjetilja Exp $

import sys
import pycurl
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

url = 'http://curl.haxx.se/dev/'

print 'Testing', pycurl.version

body = StringIO()
c = pycurl.init()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.WRITEFUNCTION, body.write)
c.perform()
c.cleanup()

contents = body.getvalue()
print contents
