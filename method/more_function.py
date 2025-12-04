
# shows function as an object.
def show():
    print('This is a function')
    
def display(a, b):
    print(a + b)
    
 
d = show 

d2 = display

d()
d2(2, 4)


# Nested function

def outer(a):
    def inner():
        print(a)
        
    inner()
    
    
outer(2)

# function as a parameter
def sum(a, b):
    print(a + b)
    
def minus(a, b):
    print(a - b)
    
def fun(f, x, y):
    f(x, y)
    
fun(sum, 2, 3)
fun(minus, 5, 4)

# returing a function
def outer2():
    def inner():
        print('This is inner function')
        
    return inner 

d2 = outer2()

d2()