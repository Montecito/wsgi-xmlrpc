#   Copyright (c) 2006-2007 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

def make_server(host='localhost', port=3423):
    import wsgi_xmlrpc
    
    def test_1():
        return 'test_1'
        
    class Test2(object):
        def test_3(self, obj):
            return obj
            
    test = Test2()
    
    application = wsgi_xmlrpc.WSGIXMLRPCApplication(instance=test, methods=[test_1])
    
    from wsgiref import simple_server
    
    server = simple_server.make_server(host, port, application)
    return server
    
def test_xmlrpc_server(uri='http://localhost:3423'):
    import xmlrpclib
    
    client = xmlrpclib.ServerProxy(uri)
    
    assert client.test_1() == 'test_1'
    assert client.test_3({'asdf':4}) == {'asdf':4}
    
if __name__ == "__main__":
    import sys
    from threading import Thread

    run = True

    try:
        server = make_server()            
        def test_wrapper():
            test_xmlrpc_server()
            run = False
            sys.exit()
        thread = Thread(target=test_wrapper)
        thread.start()
        while run:
            server.handle_request()
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()




    
