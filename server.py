import socket
import sys
import json
from threading import Thread

devices = {}
host = '127.0.0.1'
port_tcp = 33333
port_udp = 39999
buffer_size = 1024

def udp_server():
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((host, port_udp))
        print("UDP server up and listening at the: ", port_udp)
        while True:
            data, address = udp_socket.recvfrom(buffer_size)
            t = Thread(target=register_device, args=(data, address)).start()
    except Exception as error:
        print("Error")
        print(error)
        return

def tcp_server():
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((host, port_tcp))
        print("TCP server onnected!!")
        
        while True:
            tcp_socket.listen()
            client_socket, address = tcp_socket.accept()
            print("Connected to the client:", address)
            t1 = Thread(target=client_connection, args=(client_socket, address)).start()
    except Exception as error:
        print("Error")
        print(error)
        return

def client_connection(client_socket, address):
    data = client_socket.recv(buffer_size)
    devices_list = json.loads(data.decode())
    devices[address] = devices_list
    print(f"New device registered: {devices_list}")

def register_device(data, address):
    device_info = json.loads(data.decode())
    devices[address] = device_info
    print(f"New device registered: {device_info}")

def main(argv):
    udp_thread = Thread(target=udp_server)
    tcp_thread = Thread(target=tcp_server)

    udp_thread.start()
    tcp_thread.start()

    udp_thread.join()
    tcp_thread.join()

if __name__ == "__main__":
    main(sys.argv)