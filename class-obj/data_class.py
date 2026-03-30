from dataclasses import dataclass 

@dataclass
class Student:
    name: str
    id: int 
    gpa: float 
    is_passed: bool
    
s = Student('Alex', 22, 4.50, True)

print(s.__str__())