import socket

target_host = 'www.googe.com'
target_port = 80

# Cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envia alguns dados
client.sendto('AAAABBBBBCCC', (target_host, target_port))

# Recebe alguns dados
data, addr = client.recvfrom(4096)

print data