# On this file we will learn only about data types
# number(int, float, complex), boolean(True or False), String, List, diction, set, tuple

current_year = 2020
print(current_year)
next_year = current_year + 1
print(next_year)

# using type we can check the data type

print(type(2)) # int
print(type(3.14)) # float
print(type(9.81)) # float
print(type(1 + 2j)) # complex number

# Converting float to int

print(int(3.14))
print(int(9.81))
print(round(9.81))
print(float(2))

# Boolean : True or False

enjoying_lesson = True
is_light_on = True
is_single = False
value = 3 < 2
print(value)

# Strings -> strings are text data types

firstname = 'Asab'
print(firstname)
lastname = 'Yeta'

fullname = firstname + ' ' +  lastname # concatentation
print(fullname)
country = 'Finland'

print(type(firstname))
# We can use different string methods to manipulate the string

print(country.upper())
print(fullname.upper())
print('i love python because it is awesome.'.title())

# List => 
empty_list = []
print(empty_list)

numbers = [1, 2, 3, 4]
print(numbers)
print('To know the length', len(numbers))

mix_of_data_types_list = [1, 2, 'asaben', True, 9.981, 3.14, 1 +2j]
print(mix_of_data_types_list)


fruits = ['Banana','Manago', 'Avocado', 'Orange', 'Apple']
vegetables = ['Cabbage', 'Tomato', 'Potato', 'Carrot']
print(len(fruits))
fruits_and_vegs = fruits + vegetables
print(fruits_and_vegs)
