
# Take multiple variables with one key-value argument.
def fun1(*arg):
    print(*arg)
    
    
fun1()
fun1(1, 2, 3)
fun1(4, 5, 6, 7)

# unpacking the list
def fun2(a, b, c):
    print(a, b, c)
    
fun2(*[1, 2, 3])
fun2(*(2, 3, 4))
fun2(*'sky')

# multiple return values
def fun3(a, b, c):
    return a + 1, b + 2, c + 3

x, y, z = fun3(10, 22, 33)
print(x, y, z)

a = fun3(1, 2, 3)

print(a)


# we can also pass keyword argument as many as we want
def fun4(a, b, *arg, c, **kargs):
    print(a, b, c)
    print(arg)
    print(kargs)
    
fun4(10, 20, 30, 40, 50, c = 33, x = 45, y = 54, d = 85)