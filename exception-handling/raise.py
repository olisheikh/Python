
def division(a, b):
    if b != 0:
        return a //b 
    else:
        raise ZeroDivisionError
    
    
try:
    x = int(input('Enter the 1st number: '))
    y = int(input('Enter the 2nd number: '))
    
    print(division(x, y))
except:
    print('Zero division error.')