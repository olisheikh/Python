
list_name = [1, 2, 3]
print('Program Started.')

try:
    index = int(input('Enter the index number: '))
    print(list_name[index])
    print('Well done.')
except:
    print('Invalid exception')

print('Program Terminate successfully.')