#! /usr/bin/env python3
import socket, sys, re
sys.path.append("../lib")       # for params
import params


def archiver(path):
    flags = os.O_RDONLY
    
    #gets fd of the file
    fd = os.open(path, flags)
    
    #encodes name of the file to bytes
    filename = str.encode(os.path.basename(path))
    
    #gets size of tthe file
    size = os.path.getsize(fd)
    
    #gets bytearry of the content of the file
    barr = os.read(fd, size)

    #archives name of file and length of name
    barr = len(filename).to_bytes(4, byteorder = 'big') + filename + barr
    return barr


def dearchiver(barr):
    #get the len of the name of the file
    name_len = int.from_bytes(barr[:4])

    #remove the length of the name from the array
    barr = barr[4:]

    #get name of file to string
    name = str.decode(barr[:name_len])

    #open the recieved file
    recieved = os.open( name , "wb")

    #write the contents of the file
    recieved.write(barr[name_len:])

    
def send_msg(sock, msg):
    msg = len(msg).to_bytes(4) + msg
    sock.sendall(msg)

def recv_msg(sock):
    msg_len = recvall(sock, 4)
    if msg_len == 0:
        return None

def recv(sock , n):
    barr = bytearray()
    while len(barr) < n:
        packet = sock.recv(n-len(barr))
        if not packet:
            return None
        barr.extend(packet)
    return barr
    
    
switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage  = paramMap["server"], paramMap["usage"]

if usage:
    params.usage()

try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

