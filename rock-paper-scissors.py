from random import randrange

results = {
    0: 'Rock',
    1: 'Paper',
    2: 'Scissors'
}

start = input('Would you like to play Rock Paper Scissors? ')

if start.lower() == 'yes':
    print('You may enter "i quit" at any time to stop playing.')
    while True:
        i = input('\nRock, Paper, or Scissors? ')
        j = results[randrange(3)]

        if i.lower() == 'i quit':
            print('Thank you for playing.')
            break
        elif i.title() == j:
            print(f'You opponent chose {j}.')
            print('Game Tied')
        elif i.title() == 'Paper' and j == 'Rock' or i.title() == 'Rock' and j == 'Scissors' or i.title() == 'Scissors' and j == 'Paper':
            print(f'You opponent chose {j}.')
            print('You Win')
        else:
            print(f'You opponent chose {j}.')
            print('You Lose')
else:
    print('Thank you.')
