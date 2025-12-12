
class Demo:
    def __init__(self, name, email):
        self.name = name 
        self.email = email 
        
    
demo_obj = Demo('Alex', 'alex123@gmail.com')

# update the value of name
demo_obj.name = 'Bob'

print(demo_obj.name)

class Demo2:
    def __init__(self, nam, email):
        self.__nam = nam # __variable make the variable private.
        self._email = email  # _variable make the varaiale protected.
        
    def _protected_method(self, pro):
        print(f'This is {self._email}')
        self.__pri_method(pro)
        
    def __pri_method(self, pri):
        print(f'This is a privete {self.__nam}')
        
        
        
demo2_obj = Demo2('Cherry', 'cherry123@gmail.com')

demo2_obj._protected_method('Name')
