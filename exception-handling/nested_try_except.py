
try:
    a = int(input('Enter the 1st number: '))
    b = int(input('Enter the 2nd number: '))
    
    try:
        try:
            c = a // b 
            print(c)
            
        except ZeroDivisionError as ms:
            print(ms)
    except ValueError as v:
        print(v)   
except ValueError:
    print('Value error')        