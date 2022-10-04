def returnGuessResponse(guesses_left, mystery_number, user_guess):
    if user_guess != mystery_number:
        guesses_left -= 1
        if user_guess > mystery_number:
            print('Too high.')
        if user_guess < mystery_number:
            print('Too low.')
        print('guesses_left:', guesses_left)
    return guesses_left 


def userWin(mystery_number, user_guess):
    if user_guess == mystery_number:
        user_win = True
    return user_win
