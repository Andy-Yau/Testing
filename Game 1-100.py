#CODE FOR THE GAME '1-100'. Written for practice.

#initialize the answer and other variables
answer = int(input('What is the answer? '))
finish = 0
upperbound = 100    #customizable
lowerbound = 0      #customizable

#error handler for invalid answer inputs
while answer > 100 or answer < 0:
    print('Invalid answer! Try again!')
    answer = int(input('What is the answer? '))


#game starts between two players. Player A goes first.
#the loop is controlled by <finish> variable.
while finish == 0:

    #proceed to player A
    guess_A = int(input('Player A, what is your guess? '))
    if guess_A > answer:
        upperbound = guess_A
        print('Wrong guess! The range is now', lowerbound, 'to', upperbound)
    elif guess_A < answer: 
        lowerbound = guess_A
        print('Wrong guess! The range is now', lowerbound, 'to', upperbound)
    else:
        print('Player A has won the game! The answer is', answer)
        finish = 1

    if finish == 0:
        #proceed to player B
        guess_B = int(input('Player B, what is your guess? '))
        if guess_B > answer:
            upperbound = guess_B
            print('Wrong guess! The range is now', lowerbound, 'to', upperbound)
        elif guess_B < answer:
            lowerbound = guess_B
            print('Wrong guess! The range is now', lowerbound, 'to', upperbound)
        else:
            print('Player B has won the game! The answer is', answer)
            finish = 1