# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Division'
    def division(self, x, y):
        if(y != 0):
            return x / y
        else:
            return 'Division por cero'

def main():
	server = SimpleJSONRPCServer(('localhost', 5004))
	server.register_instance(Funciones())
	print("Servidor division Corriendo")
	server.serve_forever()
    
if __name__ == '__main__':  
    main()
