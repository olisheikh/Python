print('The program has started.')

list_name = [22, 33, 11]
try:
    index = int(input("Enter the index number: "))
    print(list_name[index])
    print('Well done')
    
# 1st way

# except IndexError:
#     print('Invalid index.')
    
# except ValueError:
#     print('Value error')
# except:
#     print('Some error.')

# 2nd way
except (IndexError, ValueError) as msg:
    print(msg)
except Exception as msg:
    print(msg)
print('Program Terminate successfully.')

