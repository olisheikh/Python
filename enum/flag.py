from enum import Flag

class Flag_Value(Flag):
    READ = 1
    WRITE = 2
    
p = Flag_Value.READ | Flag_Value.WRITE

print(p)