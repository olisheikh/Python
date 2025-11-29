
dict_1 = {1:'One', 2:'Two', 3:'Three'}

# Copy one dictionary items to another
dict_2 = dict_1.copy()

dict_2[2] = 'Number Two'

# Printing the id of the dictionary
print(id(dict_1[2]))
print(id(dict_2[2]))

# Update the item of the dictionary
dict_1.update({4:'Four', 5:'Five'})
print(dict_1)

dict_1[6] = 'Six'
print(dict_1)

# Sedefault will set the value if not exist
dict_2.setdefault(7, 'Seven')
print(dict_2)

name_list = ['Alex', 'Bob', 'Cherry']

studet_dict = {}

# Convert the list into the keys
studet_dict = studet_dict.fromkeys(name_list, 'New Value')
print(studet_dict)

# Pop will take one key and delete the item but not exist then delete show the msg
dict_1.pop(7, None)
print(dict_1)

# Delete an item from the end of the dictionary
dict_1.popitem()
print(dict_1)