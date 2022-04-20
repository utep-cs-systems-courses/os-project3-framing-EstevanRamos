#! /usr/bin/env python3

import SocketServer
import threading
import os

class fileTransferServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response '%s: %s' % (cur_thread.getName(),data)
        self.request.send(response)
        return

class fileTransderServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


if __name__ == '__main__':
    import socket
    import threading

    
    
