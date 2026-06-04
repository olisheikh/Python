numbers = [2, 3, 4, 5, 6]

# Lambda with map function
square = list(map(lambda x: x * x, numbers))

print(f'Square numbers: {square}')

# Lambda with filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f'Event Numbers: {even_numbers}')

exam_numbers = [
    ('Rahim', 75),
    ('Karim', 88),
    ('Jamal', 70),
]

# Lambda with sort function
highest_marks = sorted(exam_numbers, key=lambda x: x[0], reverse=True)

print(f'Highest number is: {highest_marks}')

# Lambda with dictionary
products = [
    {'name': 'Rahim', 'id': 23, 'mark': 90},
    {'name': 'Arif', 'id': 35, 'mark': 80},
    {'name': 'Badhon', 'id': 33, 'mark': 70},
    {'name': 'Jamal', 'id': 13, 'mark': 95},
]

sorted_product = sorted(products, key=lambda x: x['id'])
print(sorted_product)

# Lambda with reduct
from functools import reduce

numbers = [1, 2, 3, 4, 5]

print(reduce(lambda a, b: a * b, numbers))
