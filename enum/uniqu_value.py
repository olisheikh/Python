from enum import Enum, unique

@unique
class Uniuqe_value(Enum):
    X = 1
    Y = 10
    Z = 101
    
print(Uniuqe_value.X.value)
print(Uniuqe_value.Y.value)
print(Uniuqe_value.Z.value)