import socket
## Python 3.7 
TCP_IP = '54.80.47.180'
TCP_PORT = 5555 # > 1024 && < 65535
BUFFER_SIZE = 1024
potencia=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print ("Servidor escuchando...")

while 1:
  conn, addr = s.accept()  
  data1 = conn.recv(BUFFER_SIZE).decode("UTF-8")
  if not data1: break
  print ("Dato recibido: ", data1)
  print ("Direccion: ", addr[0])
  print ("Puerto: ", addr[1])
  conn.send("Recibido".encode("UTF-8"))

  data2 = conn.recv(BUFFER_SIZE).decode("UTF-8")
  if not data2: break
  print ("Dato recibido: ", data2)
  
  potencia=int(data1) ** int(data2)
  print ("Dato enviado: ", potencia)
  conn.send(str(potencia).encode("UTF-8"))  

  conn.close()



  
