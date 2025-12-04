
# both are allowed for every single parameter positional and keyword
def add(a, b, c, d, e, f):
    print(a, b, c, d, e, f)
    
    return sum([a, b, c, d, e, f])

add(1, 2, 3, 4, 5, 6)
add(f = 1, c = 2, e = 3, b = 10, a = 22, d = 11)


# before the '/' sign except the positional argument only.
def add2(a, b, /, c, d, e, f):
    print(a, b, c, d, e, f)
    
add2(1, 2, 3, 4, 5, 6)
add2(2, 3, c = 3, f = 33, e = 22, d = 99)


# after the '*' sign except the keyword argument only
def add3(a, b, c, d, *, e, f):
    print(a, b, c, d, e, f)
    
# add3(1, 2, 3, 4, 5, 6)
add3(1, 2, 3, 4, f = 6, e = 5)