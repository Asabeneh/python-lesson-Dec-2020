# Loops

# Print 0 to 100 using print()

# for i in range(100):
#     print('Hell world')
# for i in range(start, end, inc):
#1, 3, 6, 9

# Add all odd numbers form 1 to 100
odds= 0
print('Only odds')
for i in range(1, 101, 2):
    odds +=  i

print(odds)

# Add all evens numbers form 1 to 100
print("Only evens")
evens = 0
for i in range (0, 101, 2):
    evens +=  i

print(evens)

fruits = ['Banana','Manago', 'Avocado', 'Orange', 'Apple']
vegetables = ['Cabbage', 'Tomato', 'Potato', 'Carrot']

for fruit in fruits:
    print(fruit.upper())

i = 0
while i < 11:
    print(i)
    i = i + 1

i = 10

while i >= 0:
    print(i)
    i = i -1

# For loop and while loop