from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

pw1 = "abc12345"

hash_num = "0"

access_granted = False

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

def sign_in_function():
    import random
    random_num = random.randrange(1, 99999)
    str_random_num = str(random_num).zfill(5)
    global hash_num
    hash_num = str_random_num
    return str_random_num
server.register_function(sign_in_function, 'sign_in')

def hash_function(client_hash):
    import hashlib
    global access_granted
    string = pw1 + hash_num
    hash_value = hashlib.md5(string.encode('utf-8')).hexdigest()
    if hash_value == client_hash:
        access_granted = True
        return "access granted"
    else:
        access_granted = False
        return "access denied"
server.register_function(hash_function, 'hash_function')


test = access_granted
if access_granted == True:
    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def adder_function(x,y):
        return x + y
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'div').
    class MyFuncs:
        def div(self, x, y):
            return x // y
    server.register_instance(MyFuncs())





# Run the server's main loop
server.serve_forever()