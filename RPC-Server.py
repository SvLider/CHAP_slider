from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import random
import hashlib

pw1 = "abc12345"
user = "Sven"

hash_num = "0"
login = False


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


# Generate random number
def sign_in_function(username):
    if username == user:
        random_num = random.randrange(1, 99999)
        str_random_num = str(random_num).zfill(5)
        global hash_num
        hash_num = str_random_num
        return str_random_num
    else:
        return "0"
server.register_function(sign_in_function, 'sign_in')

# Compare login data
def check_login_function(client_user, client_hash_value):
    global login
    string = pw1 + hash_num
    hash_value = hashlib.md5(string.encode('utf-8')).hexdigest()
    
    login = client_hash_value == hash_value and client_user == user
    if login:
        server.register_function(pow_function, 'pow')
        server.register_function(adder_function, 'add')
        server.register_instance(MyFuncs())
    return login
server.register_function(check_login_function, 'check_login')



# RPC functions
def pow_function(x,y):
    return x ** y


def adder_function(x,y):
    return x + y


class MyFuncs:
    def div(self, x, y):
        return x // y

# Run the server's main loop
server.serve_forever()