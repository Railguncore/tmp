import socket
from threading import Thread

N = 2**16 - 1

for port in range(1,100):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", i, "открыт")
    except:
        continue
    finally:
        sock.close()
import socket
from threading import Thread

N = 2**16 - 1

for port in range(4998,5002):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('10.4.33.40', port))
        print("Порт", i, "открыт")
    except:
        continue
    finally:
        sock.close()
import threading
 
def proc(n):
   print "Процесс", n
 
p1 = threading.Thread(target=proc, name="t1", args=["1"])
p2 = threading.Thread(target=proc, name="t2", args=["2"])
p1.start()
p2.start()
