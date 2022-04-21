import os
import socket
import threading

#recieves files and sends it bak and server just sends it back
def handle_client(conn, addr):
    print("[thread] starting")

    # recv message
    message = conn.recv(1024)
    print("[thread] client:", addr, 'recv:', message)
    
    # send messege back
    conn.send(message)
    print("[thread] client:", addr, 'send:', message)
    
    conn.close()
    print("[thread] ending")
    

def main():
    host = '0.0.0.0'
    port = 8080

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # solution for "[Error 89] Address already in use". Use before bind()
    s.bind((host, port))
    s.listen(1)

    all_threads = []

    try:
        while True:
            print("Waiting for client")
            #once we get a new client accept it
            conn, addr = s.accept()
    
            print("Client:", addr)
        
            #start a new thread for the client
            t = threading.Thread(target=handle_client, args=(conn, addr))
            #start the thread
            t.start()
            all_threads.append(t)
    except KeyboardInterrupt:
        print("Stopped by Ctrl+C")
        
    finally:
        if s:
            s.close()
        for t in all_threads:
            #join all threads back to parent thread
            t.join()


if __name__ == '__main__':
    main()