
a = 10

def update():
    a = 15 
    # It will print the local variable
    print(a)
    
    # we can print all the local variables as a dictionary.
    print(locals())
    
update()
print(a)
    
    
# if we want to use global variable then we need to declare that before the function
a1= 10

def update():
    
    print(a1)
    
update()
print(a1)


# If we want to update the global variable then we need to add the global keyword
a3= 10

def update():
    global a3 
    a3 = 15
    print(a3)
    
update()
print(a3)

print(globals())