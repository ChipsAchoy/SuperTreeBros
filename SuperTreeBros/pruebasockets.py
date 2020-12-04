import socket, time, random
 
HOST = "localhost"
PORT = 12002
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


sock.sendall(bytes("event:avl:6:\n", 'utf-8'))

data = sock.recv(1024)
print(data)

run = True
#while run:
 
num = 2
timepassed = 0
while run:
    if timepassed % 2 == 0:
        sock.sendall(bytes("player2::"+str(random.randint(1,20))+","+"\n", 'utf-8'))
        data = sock.recv(1024)    
        print ("1)", data.decode('utf-8'))
    else:
        sock.sendall(bytes("player1::"+str(random.randint(1,20))+","+"\n", 'utf-8'))
        data = sock.recv(1024)    
        print ("2)", data.decode('utf-8'))
        
    if (data.decode('utf-8')[0:9] == "player1:f"):
        run = False
        sock.close()
        print ("Gano el player 1")
        
    elif (data.decode('utf-8')[0:9] == "player2:f"):
        run = False
        sock.close()
        print ("Gano el player 2")
        
    timepassed += 1
    num += 2
    time.sleep(1)
    
#sock.sendall(b"still waiting\n")


