import socket
host = "localhost"
ports = [80, 443]
for port in ports:
    sock = socket.socket()
    sock.settimeout(2)
    try: 
        sock.connect((host, port))
        print(f"port {port} is OPEN!")
    except:
        print(f"port {port} is CLOSED!")
    finally:
        sock.close()
