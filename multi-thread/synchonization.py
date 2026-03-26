
from threading import * 
from time import *

def display(msg):
    l.acquire()
    for i in msg:
        print(i)
        sleep(1)
    l.release()
        
        
        
l = Lock()
t1 = Thread(target=display, args=('Hello World',))
t2 = Thread(target=display, args=('Welcome',))

t1.start()
t2.start()

t1.join()
t2.join()
