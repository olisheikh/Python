class Dog:
    def __init__(self, name, breed, own):
        self.name = name 
        self.breed = breed
        self.own = own
        
    def bark(self):
        print('Whoof Whoof')
        
        
class Owner: 
    def __init__(self, name, age, mobile_number):
        self.name = name 
        self.age = age 
        self.mobile_number = mobile_number 
    

own = Owner('Alex', 22, 882)

dog_1 = Dog('Bruce', 'Terrir', own)
dog_1.bark()
print(dog_1.own.age)