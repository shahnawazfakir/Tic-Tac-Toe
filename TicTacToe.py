import random

def input_letter(letter, position):
    board[position] = letter

def tic_tac_toe_board(board_1):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def tic_tac_toe_winning_function(b, l):
    return (b[7] == l and b[8] == l and b[9] == l) or (b[4] == l and b[5] == l and b[6] == l) or (
            b[1] == l and b[2] == l and b[3] == l) or (b[1] == l and b[4] == l and b[7] == l) or (
            b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (
            b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)

def board_free_space(position):
    return board[position] == ' '

def random_move_generator(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def free_board_space(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def computer_move():
    move = 0
    moves_possible = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    for letter in ['O','X']:
        for s in moves_possible:
            copy_of_board = board[:]
            copy_of_board[s] = letter
            if tic_tac_toe_winning_function(copy_of_board, letter):
                move = s
                return move
    corner_open = []
    for i in moves_possible:
        if i in [1, 3, 7, 9]:
            corner_open.append(i)
    if len(corner_open) > 0:
        move = random_move_generator(corner_open)
        return move
    if 5 in moves_possible:
        move = 5
        return move
    edges_open = []
    for i in moves_possible:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = random_move_generator(edges_open)
    return move

def human_player_function():
    run = 1
    while run == 1:
        human_player_move = input('Select a position between 1-9 to place an \'X\': ')
        try:
            human_player_move = int(human_player_move)
            if human_player_move > 0 and human_player_move < 10:
                if board_free_space(human_player_move):
                    run = False
                    input_letter('X', human_player_move)
                else:
                    print('This space is occupied, try different position!')
            else:
                print('Please type a number within the range!')
        except ValueError:
            print('Please type a number!')

def main():
    print('Welcome to Tic Tac Toe!')
    tic_tac_toe_board(board)
    while not free_board_space(board):
        if not (tic_tac_toe_winning_function(board, 'O')):
            move = computer_move()
            if move == 0:
                print('Tie Game!')
            else:
                human_player_function()
                tic_tac_toe_board(board)
        else:
            print('The computer won this time!')
            break
        if not (tic_tac_toe_winning_function(board, 'X')):
            move = computer_move()
            if move == 0:
                print('Tie Game!')
            else:
                input_letter('O', move)
                print('Computer placed an \'O\' in position ' + str(move) + ':')
                tic_tac_toe_board(board)
        else:
            print('Congrats you won! Good Job!')
            break

while True:
    repeat_mod = None
    while repeat_mod == 'yes' or 'no':
        repeat_mod = input("Do you want to play the Tic Tac Toe (yes/no)? ")
        if repeat_mod == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            main()
        elif repeat_mod == 'no':
            print("Thanks for playing Tic Tac Toe. Have a great day!")
            exit()
        else:
            print("please enter either 'yes' or 'no'... ")