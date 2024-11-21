print('This a collection of the mini-projects I have made while learnig python')

game = input('Please choose a project from the following list: (i) Guessing Game, (ii) A Calulator, and (iii) Month Conversions: ').lower()
print(f'You have chosen {game}')

def guessing_game():
    import getpass

    secret_word = ''
    guess = ''
    guess_count = 0

    secret_word = getpass.getpass('Please enter a word for the other person to guess: ').lower()

    print('Try to guess the secret word')
    max_count = int(input('How many attempts do you want: '))
    print(f'You will have {max_count} attemps')

    while guess_count < max_count:
        guess = input('Enter guess: ').lower()
        guess_count += 1

        if guess == secret_word:
            print('Congrats, you win!')
            return  # Exit the function if the user wins
        else:
            print('Incorrect')

    print('Out of guesses')

if game == 'i' or game == 'guessing game':
    guessing_game()

    while True:
        retry = input('Would you like to try again [y/n]: ').lower()
        if retry == 'y':
            guessing_game()  # Call the function again if the user wants to retry
        elif retry == 'n':
            print('Goodbye and thanks for playing!')
            break  # Exit the loop if the user does not want to play again
        else:
            print("Please enter 'y' or 'n'")

def better_calc():
    print('This is a calculator')

    while True:
        try:
            num1 = float(input('Please enter your first number: '))
            op = input('Please select your operation: add, subtract, multiply, divide: ').lower()
            num2 = float(input('Please enter your second number: '))

            operations_key = {
                'add': lambda num1, num2: num1 + num2,
                'subtract': lambda num1, num2: num1 - num2,
                'multiply': lambda num1, num2: num1 * num2,
                'divide': lambda num1, num2: num1 / num2 if num2 != 0 else 'Divide by zero error',
            }

            # Get operation result or print error if invalid operation
            result = operations_key.get(op, lambda num1, num2: 'That is not a valid operation')(num1, num2)
            print(result)

            # Ask user if they want to clear and perform another calculation
            clear = input('Clear? [y/n]: ').lower()
            if clear == 'y':
                continue
            elif clear == 'n':
                print('Goodbye!')
                break
            else:
                print("Please enter 'y' or 'n'")

        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")
    
if game == 'ii' or game == 'a calculator':
    better_calc()

def month_conversions():
    while True:
        answer = input("Enter a month's abbreviation (e.g., Jan, Feb): ").strip().capitalize()

        month_dict = {
            'Jan': 'January', 'Feb': 'February', 'Mar': 'March',
            'Apr': 'April', 'May': 'May', 'Jun': 'June',
            'Jul': 'July', 'Aug': 'August', 'Sep': 'September',
            'Oct': 'October', 'Nov': 'November', 'Dec': 'December'
        }

        print(month_dict.get(answer, 'Invalid abbreviation. Please try again.'))

        retry = input('Try another month? [y/n]: ').lower()
        if retry == 'y':
            continue
        elif retry == 'n':
            break
        else:
            print("Please enter 'y' or 'n'")

if game == 'iii' or game == 'month conversions':
    month_conversions()

else:
    print('Thanks for playing the game!')
