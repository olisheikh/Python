from enum import Enum, auto

class A(Enum):
    ID = auto()
    COUNT = auto()
    
    
print(A.ID.value, A.COUNT.value)
print(A.ID.value, A.COUNT.value)