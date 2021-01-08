# Conditionals ->
#  

# are_enjoying_lesson = False

# if are_enjoying_lesson == True:
#       print('Then you are about to get hooked in to python')
# else:
#     print('Please gently leave the lesson.')

# a = int(input('Enter a number: '))
# if a > 0:
#     print('It is a positive number')
# elif a < 0:
#     print('It is a negative number')
# else:
#     print('The number is zero')

weather = input('Enter the weather of the day: ').lower()
if weather == 'rainy':
    print('Take raincoat')
elif weather == 'cloudy':
    print('It might be cloudy and gloomy')
elif weather == 'foggy':
    print('There might not be a good visibility of fogginess')
elif weather == 'sunny':
    print('Just a lovely day just go out freely')
else:
    print('No one knows about the weather today')

  