import socket
import threading
import time


logs = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def log_msg(msg):
    print(msg)
    logs.append(msg)

def handle_client(cli):
    if cli is not None:
        cli = cli[0]
        while len(logs) > 0:
            cli.send(logs[-1].encode('utf-8'))
            logs = logs[:-1]

def check_client():
    global sock
    try:
        cli = sock.accept()
        handle_client(cli)
    except:
        pass


def run_server():
    global sock
    print('starting server')
    sock.bind(('',1234))
    sock.listen(100000)
    sock.settimeout(5)

    #while True:
    #    check_client()
    #    time.sleep(10)

    
server = threading.Thread(target=run_server)
server.run()

print('log script done')



