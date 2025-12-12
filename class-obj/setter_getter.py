
class D:
    def __init__(self, name, email):
        self._name = name 
        self._email = email 
        
    def set_email(self, new_email):
        self._email = new_email
        
    def get_email(self):
        return self._email
    
    
demo_obj = D('Bob', 'bob123@gmail.com')
print(demo_obj.get_email())

demo_obj.set_email('bob456@gmail.com')
print(demo_obj.get_email())


class SetGet:
    def __init__(self, name, email):
        self.name = name 
        self._email = email 
        
    @property 
    def email(self):
        return self._email 
    
    @email.setter 
    def email(self, new_email):
        if '@' in new_email:
            self._email = new_email
    
    
set_get_obj = SetGet('Alex', 'alex987@gmail.com')

print(set_get_obj.email)

set_get_obj.email = 'alex9@gmail.com'

print(set_get_obj.email)