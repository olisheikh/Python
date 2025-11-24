# file read a text file.
file_name = open('demo.txt', 'r')

str_1st_line = file_name.read(10)
str_full_text = file_name.read()

print(str_full_text)
print(str_1st_line)

file_name.close()
