import random as rand


# We are going to generate a random number
# Let the user guess the number
# We copare the numbers and let them know if they got it right or not


# * define a function is_guess_right
# * greet the user and welcome them to the program
# * Display the rules of the games
# * Prompt the user to guess a number (requires input)
# ** check if the provided input is a valid number
# * check if the provided number is within range
# * Generate a random number and assign to variable
# * compare the generated number with the user's guess
# * Display whether the number was guessed correctly or not
# * Display the actual number if guess is wrong


def is_guess_right():
    print('Hello there... Are you ready to play the guessing game????? ;)')
    print('The rules are simple... Think of a number between 1 and 10.')
    print('When prompted, type that number on to the screen\nand we will tell you if your guess was correct')

    guess = input('Guess a number... And type it below\n')
    guess = int(guess)
    
    if guess >= 1 and guess <= 10:
        random_number = rand.randint(1, 10)
        if random_number == guess:
            return True
        else:
            print('The correct number is ' + str(random_number))
            return False
    else:
        return False


while(True):
    is_guess_correct = is_guess_right()
    if is_guess_correct:
        print('Great! You guessed correctly')
        print('You are a terrific guesser')
    else:
        print('Sorry better luck next time.' )
    
