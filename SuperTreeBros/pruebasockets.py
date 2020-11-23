import socket
 
HOST = "localhost"
PORT = 12002
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 
sock.sendall(b"Hello\n")
data = sock.recv(1024)
print ("1)", data)
 
if (data == "olleH\n" ):
    sock.sendall(b"Bye\n")
    data = sock.recv(1024)
    print ("2)", data)
 
    if (data == "eyB}\n"):
        sock.close()
        print ("Socket closed")

sock.sendall(b"still waiting\n")
