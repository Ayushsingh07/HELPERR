import socket
while True:
    m=input("Enter valid website address eg:www.google.com\n")
    print(socket.gethostbyname(m))
    if input("Do you want to continue")!='y':
        break
                break

