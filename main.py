
# This is a Guess the Number game program
# This is to practice variable assignments and printing statements.
import time

username = 'Javier'
password = "secret password"
username_input = input("Username: ")
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access Granted')
    print('Please wait')
    time.sleep(7)
    print('Loading....')
    time.sleep(3)
    print('...')
    print('You have clearance!')
elif username_input == username and password_input != password:
    print('Password Incorrect')
elif username_input != username and password_input == password:
    print('Username Incorrect')
else:
    print('Please check both fields...')