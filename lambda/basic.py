# A lambda is a small anonymous function in python.
# Anonymous means function without a name.

# Normal function
def add(a, b):
    return a + b

print(add(2, 3))

add_l = lambda a, b: a + b 

print(add_l(2, 2))

# Basic Sysntax lambda arguments: expression
square = lambda x: x * x

print(square(3))

# !!Important!! rules lambda function can contain only one expression
# Valid
s = lambda x, y: x + y 
print(s(2, 34))

# Invalid
# s2 = lambda x, y:
#     z = (x + y)
#     return z