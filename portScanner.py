from socket import *

q = socket(AF_INET, SOCK_STREAM)

host = input("Enter the IP you want to scan: ")
port = int(input("Enter the port you want to scan: "))

if q.connect_ex((host, port)):
    print("Port is closed!")
else:   
    print("Port is open!")
