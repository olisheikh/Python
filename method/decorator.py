
def decorat(fun):
    def inner(a, b):
        print('1st value is:', a)
        print('2nd value is:', b)
        
        c = fun(a, b)
        
        print('The summation is:', c)
    
    return inner 

@decorat
def sum(x, y):
    return x + y

# instead of calling this function we can also use the decorator

# d = decorator(sum)


sum(2, 3)