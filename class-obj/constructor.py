class DemoClass:
    def __init__(self):
        print('This is a constructor')
        

DemoClass()

demo = DemoClass()

class Student:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def info(self):
        print(self.name, self.id)
        
student_1 = Student('Alex', 22)

student_1.info()