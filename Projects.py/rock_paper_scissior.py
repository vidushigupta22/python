
import random
print('\n--------Welcome to Rock,Paper and Scissior Game--------\n')
print('*******Let"s Play*******\n')

name = input('Enter your name : ')
print(f'\n Hi {name} , the game rules are listed below 👇\n')

print(' Rock against Scissior = Rock wins 😀 \n')
print(' Rock against Paper = Rock losses 😣 \n')
print(' Scissior  against Paper = Scissior wins 😀\n')
print(' Scissior against Rock = Scissior losses 😣 \n')
print(' Paper against Rock = Paper wins 😀  \n')
print(' Paper against Scissior = Paper looses 😣  \n')

rock = 1
paper = 2
scissior = 3

winner = ''

def to_choose():
    print('Choose Your Number /n ')
    print('rock = 1')
    print('paper = 2')
    print('scissior = 3 \n')

def check_winner():
    if player_choice == 1 and comp_choice == 3:
        winner = 'Player wins - Rock'
    elif player_choice == 1 and comp_choice == 2:
        winner = 'computer wins - Paper'
    elif player_choice == 3 and comp_choice == 2:
        winner = 'Player wins - Scissior'
    elif  player_choice == 3 and comp_choice == 1:
        winner = 'Computer wins - Rock'
    elif player_choice == 2 and comp_choice == 1:
        winner = 'Player wins - Paper'
    elif player_choice == 2 and comp_choice == 3:
        winner = 'Computer wins - Scissior'
    elif player_choice == comp_choice:
        winner = 'Nobody wins - Draw 😋😋'
    
while True :
    to_choose()
    player_choice = int(input('enter your number :'))
    if player_choice == 1:
        print('Player choice = Rock')
    elif player_choice == 2:
        print('Player choice = Paper')
    elif player_choice == 3:
        print('Player choice = Scissior')
        
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        print('Computer choice = Rock')
    elif comp_choice == 2 :
        print('Computer choice = Paper')
    elif comp_choice == 3:
        print('Computer choice = Scissior')
        
        
    check_winner()
    print(winner)










    




