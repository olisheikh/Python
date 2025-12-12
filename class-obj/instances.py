
# The methods which stores an instance variable is known as the instance method.
class Demo:
    def __init__(self):
        # We can create an instance variable inside the constructor
        self.a = 22 
        
    def fun(self):
        # We can crata an instance variable inside the funciton 
        self.b = 33 
        
d = Demo()

# We can also cratea an instance variable outside the class.
d.c = 12
