# python code to get your local IP address
import socket

def get_local_ip():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.connect(("8.8.8.8",80))

        local_ip = s.getsockname()[0]

        s.close()

        return local_ip
    except Exception as e:
        print("Error",e)
        return None
    
if __name__ == '__main__':
    local_ip = get_local_ip()
    if local_ip:
        print("Local IP is %s" % local_ip)
    else:
        print("can't connect to local IP")


    

