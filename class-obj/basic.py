class MyClass:
    'A simple Example class'
    
    i = 1234
    
    def f(self):
        return 'Hello'
    
    
x = MyClass()
MyClass.i = 22

y = MyClass()

print(y.i)
print(x.i)