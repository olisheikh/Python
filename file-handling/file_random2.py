

with open('random_file.py', 'rb') as f:
    print(f.read(3).decode())
    f.seek(3, 0)
    
    print(f.read().decode())