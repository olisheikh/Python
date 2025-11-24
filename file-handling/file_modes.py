file_name = open('demo.txt', 'r+')

print(type(file_name))
print(dir(file_name))
print(file_name.name)
print(file_name.mode)
print(file_name.closed())

print(file_name.readline()) # only read a single line.
print(file_name.readlines()) # read all the lines & give a list of lines.

str_list = ['Hello, this is the 1st line.', 'Okay, I am going to include it.']

print(file_name.writelines()) # we need to give a list as a text to the parameter

file_name.close()
