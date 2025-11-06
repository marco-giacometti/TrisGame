from Tris import Status, OccupiedBoxError

game = Status()
print('\n' + str(game) + '\n')

while True:
    while True:
        try:
            print('Scegli una posizione per X (0-8):')
            pos = int(input())
            print()
            if type(pos) != int or pos not in list(range(9)):
                raise ValueError
            game.add_X(pos)
            print(str(game) + '\n')
            break
        except OccupiedBoxError:
            print('Posizione occupata\n')
        except ValueError:
            print('Posizione non valida\n')
    if game.win():
        print('THE X PLAYER WON!')
        break
    if game.tie():
        print('TIE!')
        break
    while True:
        try:
            print('Scegli una posizione per O (0-8):')
            pos = int(input())
            print()
            if type(pos) != int or pos not in list(range(9)):
                raise ValueError
            game.add_O(pos)
            print(str(game) + '\n')
            break
        except OccupiedBoxError:
            print('posizione occupata\n')
        except ValueError:
            print('Posizione non valida\n')
    if game.win():
        print('THE O PLAYER WON!')
        break
    if game.tie():
        print('TIE!')
        break

        
        
