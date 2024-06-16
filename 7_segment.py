# This program displays a given positive integer in a 7-segment LED style.
# Each digit from 0 to 9 is mapped to a predefined pattern using a dictionary.
# The program prompts the user to input a positive integer and validates the input.
# Once a valid input is provided, the program prints each digit in the 7-segment format.

# Define the 7-segment patterns for digits 0-9
pattern = {
    '0': [[' ', '#', ' '],
          ['#', ' ', '#'],
          ['#', ' ', '#'],
          ['#', ' ', '#'],
          [' ', '#', ' ']],
          
    '1': [[' ', '#', ' '],
          [' ', '#', ' '],
          [' ', '#', ' '],
          [' ', '#', ' '],
          [' ', '#', ' ']],

    '2': [['#', '#', '#'],
          [' ', ' ', '#'],
          ['#', '#', '#'],
          ['#', ' ', ' '],
          ['#', '#', '#']],

    '3': [['#', '#', '#'],
          [' ', ' ', '#'],
          ['#', '#', '#'],
          [' ', ' ', '#'],
          ['#', '#', '#']],

    '4': [['#', ' ', '#'],
          ['#', ' ', '#'],
          ['#', '#', '#'],
          [' ', ' ', '#'],
          [' ', ' ', '#']],

    '5': [['#', '#', '#'],
          ['#', ' ', ' '],
          ['#', '#', '#'],
          [' ', ' ', '#'],
          ['#', '#', '#']],

    '6': [['#', '#', '#'],
          ['#', ' ', ' '],
          ['#', '#', '#'],
          ['#', ' ', '#'],
          ['#', '#', '#']],

    '7': [['#', '#', '#'],
          [' ', ' ', '#'],
          [' ', ' ', '#'],
          [' ', ' ', '#'],
          [' ', ' ', '#']],

    '8': [['#', '#', '#'],
          ['#', ' ', '#'],
          ['#', '#', '#'],
          ['#', ' ', '#'],
          ['#', '#', '#']],

    '9': [['#', '#', '#'],
          ['#', ' ', '#'],
          ['#', '#', '#'],
          [' ', ' ', '#'],
          ['#', '#', '#']]
}

def displayLED():
    # Prompt the user for a positive integer input
    num = '-1'

    # Validate input to ensure it's a positive integer
    while not num.isnumeric() or int(num) < 0:
        num = input("Enter any Positive Integer: ")

    # Print each digit in the 7-segment LED format
    for row in range(5):
        for digit in num:
            print(''.join(pattern[digit][row]), end=' ')
        print()

# Execute the displayLED function to start the program
displayLED()
