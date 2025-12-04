
# default arguments must be right hand sight.
def add(a, b = 0, c = 0):
    return a + b + c 


print(add(2, b = 2, c = 5))


# In the case of list python won't going to create a new default list when we call without value.
def add_item(val, l1=[]):
    l1.append(val)
    print(l1)
    
    
add_item(22)
add_item(25)
add_item(32)

