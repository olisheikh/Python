from enum import Enum 

class Aliasing(Enum):
    FIRST_VALUE = 1
    SECOND_VALUE = 1
    THIRD_VALUE = 10
    
print(f'First value: {Aliasing.FIRST_VALUE.value} Address: {id(Aliasing.FIRST_VALUE.value)}')
print(f'Second vlaue: {Aliasing.SECOND_VALUE.value} Address: {id(Aliasing.SECOND_VALUE.value)}')
print(f'Third Value: {Aliasing.THIRD_VALUE.value} Address: {id(Aliasing.THIRD_VALUE.value)}')