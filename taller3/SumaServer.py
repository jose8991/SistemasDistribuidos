# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Hello word'
    def suma(self, x, y):
        return x + y

def main():
	server = SimpleJSONRPCServer(('localhost', 5001))
	server.register_instance(Funciones())
	print("Servidor addicion Corriendo")
	server.serve_forever()

if __name__ == '__main__':  
    main()
