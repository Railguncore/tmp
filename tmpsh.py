import time as t
 
def proc(n):
   print ("Процесс", n)
   t.sleep(5)
for i in range(10):
   proc(i)
