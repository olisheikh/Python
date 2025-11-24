
class Student:
    def __init__(self, roll, name, dept):
        self.roll = roll
        self.name = name
        self.dept = dept 
        
    def show(self):
        print(f'You name is {self.name}.\nYour roll is {self.roll}\nYour department is {self.dept}.\n')
        
        