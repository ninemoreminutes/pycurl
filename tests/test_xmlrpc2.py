# $Id: test_xmlrpc2.py,v 1.1 2001/08/20 15:07:45 kjetilja Exp $

## Py-XMLRPC module (get it from sourceforge.net)
import xmlrpc

## PycURL module
import pycurl

# Build request, but discard the header
req = xmlrpc.buildRequest('/RPC2', 'examples.getStateName', [5], {}).split('\r\n\r\n')[1]
c = pycurl.init()
c.setopt(pycurl.URL, 'http://betty.userland.com/RPC2')
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, req)
c.perform()
c.cleanup()
