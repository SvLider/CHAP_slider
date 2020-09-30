from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

pw1 = "abc12345"
user = "Sven"

hash_num = "0"

access_granted = True

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


# Generate random number
def sign_in_function():
    import random
    random_num = random.randrange(1, 99999)
    str_random_num = str(random_num).zfill(5)
    global hash_num
    hash_num = str_random_num
    return str_random_num
server.register_function(sign_in_function, 'sign_in')

# Compare login data
def check_login_function(client_user, client_pasword):
    if client_pasword == pw1 and client_user == "" : 
        login == True
        return login
    else: 
        login == False
        return login
server.register_function(check_login_function, 'check_login')


# Compare hash values
def hash_function(client_hash):
    global access_granted
    import hashlib
    string = pw1 + hash_num
    hash_value = hashlib.md5(string.encode('utf-8')).hexdigest()
    if hash_value == client_hash:
        access_granted = True
        return "access granted"
    else:
        access_granted = False
        return "access denied"
server.register_function(hash_function, 'hash_function')


# RPC functions
if access_granted == True:
    
    server.register_function(pow)
    
    def adder_function(x,y):
        return x + y
    server.register_function(adder_function, 'add')

    class MyFuncs:
        def div(self, x, y):
            return x // y
    server.register_instance(MyFuncs())
else:
     print("Login Daten falsch")




# Run the server's main loop
server.serve_forever()