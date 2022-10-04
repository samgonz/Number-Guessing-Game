
from random import randint
import splashScreen
import guessResponse

guesses_left = 5
mystery_number = randint(1, 100)
user_win = False

print(splashScreen.logo)

# Loop through the guesses
while guesses_left > 0 or user_win == True:
    """Asks the user to choose a number. If the user selects the correct number then they win
    Otherwise they guess the number again and they get 1 less guess.
    Game over is when the user guesses the number or they fail to guess.
    """    
    user_guess = int(input('Please enter your guess from 1 - 100.\n'))
    
    guesses_left = guessResponse.returnGuessResponse(guesses_left, mystery_number, user_guess)
    
    if user_guess == mystery_number:
        user_win = True
# Print out the results of the game
if user_win == True:
    print('User has guessed the correct answer.')
if user_win == False:
    print(f'User has not guessed the correct answer. The correct answer was {mystery_number}')
    