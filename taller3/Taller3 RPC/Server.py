# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from jsonrpclib import Server

#puertos de los servidores
servers = {
    'suma' : 5001,
    'resta' : 5002,
    'multiplicacion' : 5003,
    'division' : 5004,
    'pot' : 5005,
    'logaritmo' : 5006
}

class Funciones:
    Cadena = ''
    def __init__(self):
        self.Cadena = 'Hello word'
        self.conn = 'http://localhost:'
    def sum(self, x, y):
        server = Server(self.conn+str(servers['suma']))
        return server.suma(x,y)
    def rest(self, x, y):
        server = Server(self.conn+str(servers['resta']))
        return server.resta(x,y)
    def mult(self, x, y):
        server = Server(self.conn+str(servers['multiplicacion']))
        return server.multiplicacion(x,y)
    def div(self, x, y):
        server = Server(self.conn+str(servers['division']))
        return server.division(x,y)
    def pot(self, x, y):
        server = Server(self.conn+str(servers['pot']))
        return server.potencia(x,y)
    def log(self, x, y):
        server = Server(self.conn+str(servers['logaritmo']))
        return server.logaritmo(x,y)

def main():
	server = SimpleJSONRPCServer(('localhost', 5000))
	server.register_instance(Funciones())
	print("Servidor Intermedio Corriendo")
	server.serve_forever()
if __name__ == '__main__':  
    main()
