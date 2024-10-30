import socket

NODEMCU_IP = '192.168.43.58'
NODEMCU_PORT = 80

def conn(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((NODEMCU_IP, NODEMCU_PORT))
        data_to_send = message
        sock.sendall(data_to_send.encode())
        
        response = sock.recv(1024)  # Buffer size is 1024 
        #print("Response from NodeMCU:", response.decode())
    except Exception as e:
        print("Error:", e)

    finally:
        sock.close()
        print("Connection closed.")

