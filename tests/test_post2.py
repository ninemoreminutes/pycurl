# $Id: test_post2.py,v 1.8 2002/08/18 20:27:26 kjetilja Exp $

import pycurl


pf = ['field1=this is a test using httppost & stuff', 'field2=value2']

c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.sourceforge.net/tests/testpostvars.php')
c.setopt(c.HTTPPOST, pf)
c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
