import socket
import json

host = '127.0.0.1'
port_udp = 39999
buffer_size = 1024

def main():
    try:
        device_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        device_info = [{"device_type": "ar", "settings": ["alto", "branco"]},
                    {"device_type": "lam", "settings": ["25°C"]}]

        for info in device_info:
            print(info)
            device_socket.sendto(json.dumps(info).encode(), (host, port_udp))
            server_message = device_socket.recvfrom(buffer_size)
            print("Message from server: {}".format(server_message[0]))
    except Exception as error:
        print("Error:")
        print(error)

if __name__ == "__main__":
    main()
