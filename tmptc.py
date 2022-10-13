import time as t
import threading

class T(threading.Thread):
  def __init__(self, n):
    threading.Thread.__init__(self, name="t" + n)
    self.n = n

  def run(self):
    print ("Процесс", self.n)
    t.sleep(5)
p=[]
for i in range(10):
    p.append(T(str(i)))
    p[i].start()
