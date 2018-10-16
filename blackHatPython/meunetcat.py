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
    
        
main()