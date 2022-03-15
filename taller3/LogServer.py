# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from math import log 

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Logaritmica'
    def logaritmo(self, x, y):
        return log(x, y)

def main():
	server = SimpleJSONRPCServer(('localhost', 5006))
	server.register_instance(Funciones())
	print("servidor logaritmo Corriendo")
	server.serve_forever()
if __name__ == '__main__':  
    main()
