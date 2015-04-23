## Example ##

Below is an example server using wsgiref (available in stdlib as of python2.5)

```
from wsgiref import simple_server
import wsgi_xmlrpc
    
class Methods(object):
    def test_1(self):
        return u'test_1'
    def test_2(self, value):
        return value
            
def test_3()
    return 'test3'

methods = Methods()
    
application = wsgi_xmlrpc.WSGIXMLRPCApplication(instance=methods, methods=[test_3])
server = simple_server.make_server('localhost', 80, application)
server.serve_forever()
```