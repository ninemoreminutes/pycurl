#! /usr/bin/env python
# vi:ts=4:et
# $Id: test_post2.py,v 1.10 2002/11/19 13:37:27 kjetilja Exp $

import pycurl


pf = ['field1=this is a test using httppost & stuff', 'field2=value2']

c = pycurl.Curl()
c.setopt(c.URL, 'http://www.contactor.se/~dast/postit.cgi')
c.setopt(c.HTTPPOST, pf)
c.setopt(c.VERBOSE, 1)
c.perform()
c.close()
