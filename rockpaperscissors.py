import random
currentscore = 0

while True:
    playermove = True

    while playermove == True:
        print('What is your move? Rock, paper, or scissors?')
        playerhand = input()
        playermove = False
    while playermove == False:
        comphand = random.randint(1,3)
        if comphand == 1:
            comphand = 'paper'
            print('Computer plays paper.')
            if comphand == playerhand:
                print('Draw\nCurrentscore is' + ' ' + str(currentscore))
            elif playerhand == 'scissors':
                currentscore += 1
                print('You win.')
                print('Currentscore is ' + ' ' + str(currentscore))
            elif playerhand == 'rock':
                currentscore += -1
                print('You lose.')
                print('Currentscore is' + ' ' + str(currentscore))
        elif comphand == 2:
            comphand = 'rock'
            print('Computer plays rock.')
            if comphand == playerhand:
                print('Draw')
                print('Currentscore is' + ' ' + str(currentscore))
            elif playerhand == 'scissors':
                currentscore += -1
                print('You lose.')
                print('Currentscore is' + ' ' + str(currentscore))
            elif playerhand == 'paper':
                currentscore += +1
                print('You win.')
                print('Currentscore is' + ' ' + str(currentscore))
        elif comphand == 3:
            comphand = 'scissors'
            print('Computer plays scissors.')
            if comphand == playerhand:
                print('Draw')
            elif playerhand == 'paper':
                currentscore += -1
                print('You lose.')
                print('Currentscore is' + ' ' + str(currentscore))
            elif playerhand == 'rock':
                currentscore += 1
                print('You win.')
                print('Currentscore is' + ' ' + str(currentscore))
        playermove = True







