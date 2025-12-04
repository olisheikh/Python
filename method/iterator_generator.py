
# Iteration to iterate through the list
l1 = [1, 2, 3, 4, 5]
it = iter(l1)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# Iterate through the dictionary only gives the key.
d1 = {1: 'One', 2: 'Two', 3: 'Three'}
itd = iter(d1)

print(next(itd))
print(next(itd))
print(next(itd))

# Generator function. 
def gen():
    l1 = ['Samstag', 'Sonstag', 'Montag', 'Dienstag', 'MittWoch', 'Donnerstag', 'Frietag']
    i = 0
    
    while True:
        x = l1[i]
        i = (i + 1) % 7 
        yield x 
        
        
itg = gen()
print(next(itg))
print(next(itg))
print(next(itg))
print(next(itg))
print(next(itg))
print(next(itg))
print(next(itg))
print(next(itg))
print(next(itg))