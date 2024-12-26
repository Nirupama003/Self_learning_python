import random,sys

print("ROCK, PAPER, SCISSORS!!!")
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins, %s losses, %s ties ' %(wins,losses,ties))
    while True:
        print('enter your move : (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('type one of r, p, s or q.')

    if player_move == 'r':
        print('ROCK verses...')
    elif player_move == 'p':
        print("PAPER verses...")
    elif player_move == 's':
        print("SCISSORS verses...")

    randomNum= random.randint(1,3)

    if randomNum == 1:
        computermove = 'r'
        print('ROCK')

    elif randomNum == 2:
        computermove = 'p'
        print("PAPER")

    elif randomNum == 3:
        computermove = 's'
        print("SCISSORS")


    if player_move == computermove:
        print("It is a Tie!")
        ties += 1
    elif player_move == 'r'and computermove == 's':
        print("You Win!")
        wins += 1

    elif player_move == 'r' and computermove == 'p':
        print("you loss!")
        losses +=1
    elif player_move == 'p' and computermove == 'r':
        print("you win!")
        wins += 1
    elif player_move == 'p' and computermove == 's':
        print("you loss!")
        losses += 1
    elif player_move == 's' and computermove == 'r':
        print("you loss!")
        losses +=1
    elif player_move == 's' and computermove == 'p':
        print("you win!")
        win += 1
        
        
        
    
