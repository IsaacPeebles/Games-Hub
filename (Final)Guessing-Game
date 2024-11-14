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

# Start the game for the first time
guessing_game()

# Ask if the user wants to play again
while True:
    retry = input('Would you like to try again [y/n]: ').lower()
    if retry == 'y':
        guessing_game()  # Call the function again if the user wants to retry
    elif retry == 'n':
        print('Goodbye and thanks for playing!')
        break  # Exit the loop if the user does not want to play again
    else:
        print("Please enter 'y' or 'n'")

guessing_game()