from random import randrange
field = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]




end_game = False


def player(field):
    can_player_turn = False
    print('Player turn')
    print(*field, sep='\n')
    while can_player_turn == False:
        try:
            x, y = int(input()), int(input())
            try:
                if field[x][y] == 'X' or field[x][y] == '0':
                    print('Try again')
                    continue
                else:
                    can_player_turn = True
                    field[x][y] = 'X'

            except IndexError:
                print('Not correct coord')
                continue
        except ValueError:
            print('Not correct coord')
            continue

def comp(field):
    can_comp_turn = False
    while can_comp_turn == False:
        x, y = randrange(3), randrange(3)
        if field[x][y] == 'X' or field[x][y] == '0':
            continue
        else:
            can_comp_turn = True
            field[x][y] = '0'

def check_win_with_computer(field):
    player_win = False
    computer_win = False
    if (field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X') or (
            field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X') or (
            field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X') or (
            field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X') or (
            field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X') or (
            field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X') or (
            field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X') or (
            field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X'):
        player_win = True
        print('Player Win')
        return player_win

    elif (field[0][0] == '0' and field[0][1] == '0' and field[0][2] == '0') or (
            field[1][0] == '0' and field[1][1] == '0' and field[1][2] == '0') or (
            field[2][0] == '0' and field[2][1] == '0' and field[2][2] == '0') or (
            field[0][0] == '0' and field[1][1] == '0' and field[2][2] == '0') or (
            field[0][2] == '0' and field[1][1] == '0' and field[2][0] == '0') or (
            field[0][0] == '0' and field[1][0] == '0' and field[2][0] == '0') or (
            field[0][1] == '0' and field[1][1] == '0' and field[2][1] == '0') or (
            field[0][2] == '0' and field[1][2] == '0' and field[2][2] == '0'):
        computer_win = True
        print('Computer Win')
        return computer_win

def game_with_comp(field):
    a = 0
    while a<4:
        player(field)
        comp(field)
        a+=1
        if check_win_with_computer(field) == True:
            break

    if a>=4:
        player(field)
        if check_win_with_computer(field) == False:
            print('Draw')

def player1(field):
    can_player_turn = False
    print('Player1 turn')
    print(*field, sep='\n')
    while can_player_turn == False:
        try:
            x, y = int(input('Player1 X')), int(input('Player2 Y'))
            try:
                if field[x][y] == 'X' or field[x][y] == '0':
                    print('Try again')
                    continue
                else:
                    can_player_turn = True
                    field[x][y] = 'X'
                    print(*field, sep='\n')
            except IndexError:
                print('Not correct coord')
                continue
        except ValueError:
            print('Not correct coord')
            continue

def player2(field):
    can_player_turn = False
    print('Player2 turn')
    print(*field, sep='\n')
    while can_player_turn == False:
        try:
            x, y = int(input('Player2 X')), int(input('Player2 Y'))
            try:
                if field[x][y] == 'X' or field[x][y] == '0':
                    print('Try again')
                    continue
                else:
                    can_player_turn = True
                    field[x][y] = '0'
                    print(*field, sep='\n')
            except IndexError:
                print('Not correct coord')
                continue
        except ValueError:
            print('Not correct coord')
            continue

def check_win_with_player(field):
    player1_win = False
    player2_win = False
    if (field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X') or (
            field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X') or (
            field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X') or (
            field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X') or (
            field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X') or (
            field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X') or (
            field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X') or (
            field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X'):
        player1_win = True
        print('Player1 Win')
        return player1_win

    elif (field[0][0] == '0' and field[0][1] == '0' and field[0][2] == '0') or (
            field[1][0] == '0' and field[1][1] == '0' and field[1][2] == '0') or (
            field[2][0] == '0' and field[2][1] == '0' and field[2][2] == '0') or (
            field[0][0] == '0' and field[1][1] == '0' and field[2][2] == '0') or (
            field[0][2] == '0' and field[1][1] == '0' and field[2][0] == '0') or (
            field[0][0] == '0' and field[1][0] == '0' and field[2][0] == '0') or (
            field[0][1] == '0' and field[1][1] == '0' and field[2][1] == '0') or (
            field[0][2] == '0' and field[1][2] == '0' and field[2][2] == '0'):
        player2_win = True
        print('Player2 Win')
        return player2_win

def game_with_player(field):
    a = 0
    while a<4:
        player1(field)
        player2(field)
        a+=1
        if check_win_with_player(field) == True:
            break

    if a>=4:
        player1(field)
        if check_win_with_player(field) == False:
            print('Draw')




while True:
    print('1.Game with computer\n2.Game with player')
    choose = int(input('Choose mode: '))
    if choose == 1:
        game_with_comp(field)
    elif choose == 2:
        game_with_player(field)
    else:
        continue