import socket
# Code from Digital Ocean and GeeksForGeeks referenced heavily

def Server():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection

    print("Connection from: " + str(address))

    fileno = 0 # show which file the server gets
    filename = 'output' + str(fileno)+'.txt'
    fileno = fileno + 1
    fo = open(filename, "w")
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        if(data == "sharefile"):
            while data:
                data = conn.recv(1024).decode()
                print("Writing data")
                fo.write(data) #write 1024 bytes to the file
                break

        print("File Write done back to messaging.")
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    Server()