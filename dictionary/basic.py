
dict_name = {1: 'One', 2: 'Two', 3: 'Three'}

print(dict_name)

print(dict_name[1])

for i in dict_name:
    print(i, dict_name[i])
    
print(dict_name.get(2))

print(dict_name.get(4, 'Invalid Key')) # return the value but if the key is present return the msg.

print(dict_name.keys()) # return all the keys as list

print(dict_name.values()) # return all the values as list

print(dict_name.items()) # return the key-value pair in the tuple