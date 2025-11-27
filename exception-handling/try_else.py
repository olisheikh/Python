
try:
    x = int(input('Enter the 1st number: '))
    y = int(input('Enter the 2nd number: '))
    
    z = x//y 
    
except ZeroDivisionError as msg:
    print(msg)
else:
    print('Your result is : ', z)