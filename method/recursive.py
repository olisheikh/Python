
def fact(num):
    if num == 0:
        return 1 
    else:
        res = num * fact(num - 1)
        return res 
    
    
r = fact(int(input('Enter a number: ')))
print(r)