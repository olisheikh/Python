
# Thread with thread object

from threading import * 

def display():
    for i in range(65, 91):
        print(chr(i))
        
    
t = Thread(target=display, name='Alpha')
t.start()

for i in range(65, 91):
    print(i)
    
t.join()

# Thread with class 
class Alphabet(Thread):
    def run(self):
        for j in range(65, 91):
            print(chr(j))
            
            
th = Alphabet()

th.start()

for j in range(65, 91):
    print(j)
    
th.join()