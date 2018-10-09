import socket
import signal

target_host = '0.0.0.0'
target_port = 9999

# Cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o cliente se conectar
client.connect((target_host, target_port))

time.sleep(1)

# Envia alguns dados
client.send('GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n'.encode())

# Recebe alguns dados
response = client.recv(4096)

print (response)