#! /usr/bin/env python3
import socket, sys, re, os, struct
from arc import archiver , dearchiver



def send_msg(sock, msg):
    msg = len(msg).to_bytes(4, 'big') + msg
    sock.sendall(msg)

def recv_msg(sock):
    msg_len = recvall(sock, 4)
    msg_len = int.from_bytes(msg_len, 'big')
    if msg_len == 0:
        return None
    return recvall(sock , msg_len)

def recvall(sock , n):
    barr = bytearray()
    while n:
        packet = sock.recv(n)
        if not packet:
            return None
        barr.extend(packet)
        n -= len(packet)
    return barr


def main():
    PATH = 'test.txt'
    HOST = '0.0.0.0'
    PORT = 8080
    
    
    # instantiate a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket instantiated')

    # connect the socket
    connectionSuccessful = False
    while not connectionSuccessful:
        try:
            sock.connect((HOST, PORT))    # Note: if execution gets here before the server starts up, this line will cause an error, hence the try-except
            print('socket connected')
            connectionSuccessful = True
        except:
            print('socket unsucesfull')
            pass
    
    msg_sent = False
    try:
        #try to send file
        print('sending messege...')
        barr = archiver(PATH)
        send_msg(sock, barr)
        msg_sent = True
    except:
        pass
    
    
    if msg_sent:
        print('recieving messege...')
        barr = recv_msg(sock)
        dearchiver(barr)
    else:
        print('sending messege unsuccessful...')
        
        
if __name__ == '__main__':
    main()
    