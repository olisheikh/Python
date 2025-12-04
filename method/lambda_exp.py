
s = lambda a, b: a + b 
voter = lambda age: True if age > 18 else False 

print(s(2, 3))
print('You are a voter:', voter(28))