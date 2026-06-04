# lambda with one argument
double_value = lambda x: x * 2

print(double_value(2))

# lambda with multiple arguments
summation = lambda a, b, c, d: (a + b + c) // b
print(summation(2, 3, 4, 5))

# lambda with default arguments
addition = lambda a=22, b=2: a + b
print(addition(3))