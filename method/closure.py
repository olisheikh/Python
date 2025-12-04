
# Nested function, accessing non-local value, and return nested function 
def outer():
    msg = 'Hello'
    
    def inner():
        print('*****')
        print(msg)
        print('*****')
        
    return inner

m = outer()

m()

# Nested function, accesing local variables as a parameter, and return a function
def outer2(msg):
    def inner2():
        print('Inner 2 start')
        print(msg)
        print('Inner 2 end')
    return inner2

m2 = outer2('Bye')
m2()

# Caller class

# With class

class Caller:
    def __init__(self):
        self.dept_name = {'hr': 'Human Resource Department',
                     'acc': 'Account and Finance Department',
                     'sd': 'Sales and Marketing Department',
                     'mft': 'Manufacturing Department'}
    def __call__(self, dept):
        print(f'This is a {self.dept_name[dept]}')
        
cobj = Caller()

cobj('hr')
cobj('sd')

# Caller class with function
def caller2():
    dept_name2 = {'hr': 'Human Resource Department',
                     'acc': 'Account and Finance Department',
                     'sd': 'Sales and Marketing Department',
                     'mft': 'Manufacturing Department'}
    def name_dep(dept):
        return dept_name2[dept]
    
    return name_dep

d3 = caller2()

print(d3('hr'))
print(d3('acc'))