# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Potencia Server'
    def potencia(self, x, y):
        return x ** y

def main():
	server = SimpleJSONRPCServer(('localhost', 5005))
	server.register_instance(Funciones())
	print("Potencia Server Corriendo")
	server.serve_forever()
if __name__ == '__main__':  
    main()
