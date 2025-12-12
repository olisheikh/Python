
class Demo2:
    count = 0 
    
    def __init__(self):
        print('Constructor')
        self.a = 22
        Demo2.count += 1
        
    def fun(self):
        print(self.a)
        
    def st(cls):
        print(cls.count)
        
    @staticmethod
    def sta(l, b):
        print(l, b)
        
        

d2 = Demo2()
d2.st()
d2.sta(2, 3)

Demo2.sta(33, 22)