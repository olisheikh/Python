# IndexError -> when we try to use a non-existing index.
list_name = [1, 2, 3]

print(list_name[2]) # 3
print(list_name[3]) # Throw a IndexError: list index out of range

# Value error
age = int('12')
age2 = int('abc') # ValueError: invalid literal for int() with base 10: 'abc'

# TypeError 
a = 10
b = 'abc'

c = a + b # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# KeyError
d = {1:'a', 2:'b'}
print(d[1])
print(d[3]) # KeyError: 3

