import time


def loop():
    loop()


try:
    operation = input('''
Welcome To Calculator Ver1.1 By Lochlan Ford
Please type in what maths symbol you would like to use
+ to add
- to minus
* to multiply
/ to divide
''')

    number_1 = int(input('first number plz: '))
    number_2 = int(input('second number plz: '))

# Add
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

# Minus
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

# Multiply
    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2))
        print(number_1 * number_2)

# Divide
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed one of the 4 symbols')
        print('What are you doing?')
        print('How do you mess that up?')
        print('To try again re-run the program')
        print('And dont fuck it up next time')

    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        loop()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        loop()
except KeyboardInterrupt:
    print('''Hey, you have pressed Ctrl+C or Delete key 
which has caused an error, The program will now restart''')
time. sleep(1)
print('3')
time. sleep(1)
print('2')
time. sleep(1)
print('1')
time. sleep(1)
print('Restarting Now')
time. sleep(1)
loop()
