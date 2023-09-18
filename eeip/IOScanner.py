import socket

def eeipScanner(broadcast_address, discovery_port, timeout=10, recvbuf=1024):
    #broadcast_address = '192.168.1.100'  #TODO: this should be dynamic
    #discovery_port = 44818  #EthernetIP Port
  
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Define the discovery message
    discovery_message = "DeviceDiscoveryRequest"
    device_responses = []
    try:
        sock.sendto(discovery_message.encode(), (broadcast_address, discovery_port))
        sock.settimeout(timeout)  # timeout for receiving responses - dynamic?
        while True:
            try:
                response, addr = sock.recvfrom(recvbuf)
                device_responses.append([addr, response.decode()])
            except socket.timeout:
                break  # Stop listening after timeout
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        sock.close()
    return device_responses
