import pycurl

def data(*args, **kwargs):
    print args, kwargs


stream = pycurl.Curl()
stream.setopt(pycurl.INTERLEAVEFUNCTION, data)
stream.setopt(pycurl.RTSP_REQUEST, pycurl.CURL_RTSPREQ_DESCRIBE)
stream.setopt(pycurl.URL, "rtsp://192.168.137.66/axis-media/media.amp")
#stream.setopt(pycurl.URL, "rtsp://192.168.137.66/mpeg4/1/media.amp")
stream.perform()