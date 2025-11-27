
def div(x, y):
    try:
        z = x // y
        return z
    
    except ZeroDivisionError as msg:
        raise ZeroDivisionError
    
    finally:
        print('Finally Block')
        
z = div(10, 2)
print(z)
z = div(10, 0)
print(z)