import socket
import json

host = '127.0.0.1'
port_tcp = 33333
buffer_size = 1024

def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port_tcp))
        print("Connected to the server")

        while True:
            print("\n1. List Devices\n2. Configure Device\n3. Quit")
            option = int(input("Choose an option: "))

            if option == 1:
                list_devices(client_socket)
            elif option == 2:
                configure_device(client_socket)
            elif option == 3:
                print("Exiting user application.")
                break
            else:
                print("Invalid option. Try again!!")

    except Exception as error:
        print("Error connecting to the server!!")
        print(error)
        return

def list_devices(client_socket):
    try:
        request = {"action": "list_devices"}
        client_socket.send(json.dumps(request).encode())

        response = client_socket.recv(buffer_size).decode()
        devices_list = json.loads(response)  

        print("List of Devices:")
        if isinstance(devices_list, list):
            for device in devices_list:
                print(device)
        else:
            print("Unexpected response format:", response)

    except Exception as error:
        print("Error listing devices:")
        print(error)


def configure_device(client_socket):
    try:
        device_type = input("Enter the device type to configure: ")
        new_settings = input("Enter the new settings for the device: ")

        # Send a request to the server to configure the device
        request = {"action": "configure_device", "type": device_type, "new_settings": new_settings}
        client_socket.send(json.dumps(request).encode())

        # Receive and print the response from the server
        response = client_socket.recv(buffer_size).decode()
        print(response)

    except Exception as error:
        print("Error configuring device:")
        print(error)

if __name__ == "__main__":
    main()
