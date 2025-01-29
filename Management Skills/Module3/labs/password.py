# FIXME (1): Finish reading another word and an integer into variables. 




# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
second_word = input()
number = input()

print('You entered: {} {} {}'.format(favorite_color, second_word, number))

# FIXME (2): Output two password options
password1 = '{}_{}'.format(favorite_color, second_word)
password2 = '{}{}{}'.format(number, favorite_color, number)'

print('\nFirst password: {}_{}'.format(favorite_color, second_word))
print('Second password: {}{}{}'.format(number, favorite_color, number))


# FIXME (3): Output the length of the two password options
length1 = len(password1)
length2 = len(password2)
print('\nNumber of characters in {}: {}'.format(password1, length1))
print('Number of characters in {}: {}'.format(password2, length2))