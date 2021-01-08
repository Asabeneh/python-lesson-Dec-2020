# Functions: are a set of codes that performs a certain task

# Builtin-function and methods

print('Hello World')
gravity = round(9.81)
print(type(9.81))
print(gravity)
print(type(gravity))
print(int(9.81))
print(sum([1, 2, 3, 4]))

# numbers = list(range(101))
# print(numbers)
# evens = list(range(0, 10000, 2))
# print(evens)
# Custom function

def do_something ():
    print('Of course, I am doing something at least I am teaching some people')

do_something()


def add_two_numbers (a, b):
   return a + b



print(add_two_numbers(1, 2))
print(add_two_numbers(3, 2))

# Make a function which changes number to its square
def make_square (n):
    return n ** 2


print(make_square(3))
print(make_square(4))

# print_fullname, it takes firstname, lastname as a parameter and it returns the fullname of a person

def print_fullname (firstname = 'Asab', lastname = 'Yet'):
    return firstname + ' ' + lastname

print(print_fullname('John', 'Doe'))


# Write a function which adds all odd numbers

def add__odd_numbers (n):
    sum_odds = 0
    for i in range(1, n + 1, 2):
        sum_odds = sum_odds + i
    return sum_odds

print(add__odd_numbers(100))

def add__even_numbers (n):
    sum_evens = 0
    for i in range(0, n + 1, 2):
        sum_evens = sum_evens + i
    return sum_evens

print(add__even_numbers(100))

print(print_fullname())

def multiple_two_numbers (a = 10, b = 1):
    return a * b

print(multiple_two_numbers())

def calculate_weight (mass, gravity = 9.81):
    return f'{mass * gravity} N'

print(calculate_weight(75, 3.71))

