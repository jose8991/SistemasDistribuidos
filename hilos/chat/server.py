import socket
import threading
import sys
import pickle
class Servidor():
    def __init__(self,host="localhost",port=9000):
        self.clientes=[]
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind(str(host),int(port))
        self.sock.listen(5)
        self.sock.setblocking(False)
        #hilo para aceptar la conexiones
        aceptar=threading.Thread(target=self.aceptarCon)
        procesar=threading.Thread(target=self.procesarCon)
        aceptar.daemon= True
        aceptar.start()
        procesar.daemon=True
        procesar.start()
        while True:
            msg=input('-->')
            if msg == 'exit':
                self.sock.close()
                sys.exit()
            else:
                pass
    def msgToAll(self,msg,cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send()
            except:
                self.clientes.remove(c)
            
    def aceptarCon(self):
        while True:
            try:
                conn,addr=self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
            except:
                pass
    def procesarCon(self):
        print("procesando conexion")
        while True:
            if len(self.clientes)>0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        if data:
                            self.msgToAll(data,c)
                    except:
                        pass
s=Servidor()

