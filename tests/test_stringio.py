# $Id: test_stringio.py,v 1.3 2002/08/06 19:59:54 mfx Exp $

import sys
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
import pycurl

url = 'http://curl.haxx.se/dev/'

print 'Testing', pycurl.version

body = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, body.write)
c.perform()
c.close()

contents = body.getvalue()
print contents
