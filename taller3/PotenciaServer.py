# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Potencia'
    def potencia(self, x, y):
        return x ** y

def main():
	server = SimpleJSONRPCServer(('localhost', 5005))
	server.register_instance(Funciones())
	print("servidor potencia corriendo")
	server.serve_forever()
if __name__ == '__main__':  
    main()
