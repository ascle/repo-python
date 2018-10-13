# -*- coding: utf-8 -*-
import socket
import threading

# Esta é a thread para tratamento de clientes
def handle_client(client_socket):
  request = client_socket.recv(1024)
  print ('[*] Received: %s' %request)
  #Envia o pacote de volta
  client_socket.send('ACK!')
  client_socket.close()
  
bind_ip = '0.0.0.0'
bind_porta = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço e porta q queremos q o servidor fique ouvindo
server.bind((bind_ip, bind_porta))
# Comece escultar, no maximo 5 conexoes
server.listen(5)
print ('[*] Listening on: %s:%d' %(bind_ip, bind_porta))

while True:
  # Cliente se conecta
  client, addr = server.accept()
  print ('[*] Accepted conection from: %s:%d' %(addr[0], addr[1]))
  
  #coloca nossa thread de cliente em ação para tratar dados de entrada
  client_handler = threading.Thread(target=handle_client, args=(client,))
  client_handler.start()


    
