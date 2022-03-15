# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Resta'
    def resta(self, x, y):
        return x - y

def main():
	server = SimpleJSONRPCServer(('localhost', 5002))
	server.register_instance(Funciones())
	print("servidor resta corriendo")
	server.serve_forever()
if __name__ == '__main__':  
    main()
