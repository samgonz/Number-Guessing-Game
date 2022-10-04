
from random import randint
import splashScreen
import guessResponse

print(splashScreen.logo)

user_difficulty = input('What difficulty you would like? 1[easy] - 5[hard]\n')
guesses_left = 8 - int(user_difficulty)
mystery_number = randint(1, 100)
user_win = False

# Loop through the guesses
while guesses_left > 0 and user_win == False:
    """Asks the user to choose a number. If the user selects the correct number then they win
    Otherwise they guess the number again and they get 1 less guess.
    Game over is when the user guesses the number or they fail to guess.
    """    
    user_guess = int(input('Please enter your guess from 1 - 100.\n'))
    
    # Adjusts the guesses left and gives the user a hint
    guesses_left = guessResponse.returnGuessResponse(guesses_left, mystery_number, user_guess)
    
    # Checks to see if user wins
    user_win = guessResponse.userWin(mystery_number, user_guess)
    
# Print out the results of the game
if user_win == True:
    print('User has guessed the correct answer.')
if user_win == False:
    print(f'User has not guessed the correct answer.\nThe correct answer was {mystery_number}')
    