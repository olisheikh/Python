from enum import Enum 

class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    

print(Status.APPROVED.name)
print(Status.REJECTED.value)
print(Status(2))
print(Status(Status.APPROVED))

from enum import IntEnum

class Level(IntEnum):
    LOW = 1
    HIGH = 2
    
print(Level.LOW)
print(Level.HIGH.name)
print(Level.HIGH.value)

for status in Status:
    print(status.name)
    print(status.value)