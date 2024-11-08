import random
board = [
" ", " ", " ", 
" ", " ", " ", 
" ", " ", " "]

print("""
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9""")

player = 0
bot = 0
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def tie_check():
    i = 0
    for play in board:
        if play == "X" or play == "O":
            i += 1
    if i != 9:
        i = 0
    return i == 9
def win_check(XO):
    x_win = 0
    o_win = 0
    for win in wins:
        for play in win:
            if board[play] == " ":
                x_win = 0
                o_win = 0
                break
            elif board[play] == "X":
                x_win += 1
            elif board[play] == "O":
                o_win += 1
        
        if XO == "O":
            if o_win == 3:
                x_win = 0
                o_win = 0
                return "O"
            else:
                x_win = 0
                o_win = 0
        if x_win == 3:
            x_win = 0
            o_win = 0
            return "X"
        else:
            x_win = 0
            o_win = 0
        if XO == "O":
            if o_win == 3:
                x_win = 0
                o_win = 0
                return "O"
            else:
                x_win = 0
                o_win = 0
    return " "
def print_board():
    print(f"""Current board: 
{board[0]} | {board[1]} | {board[2]}
{board[3]} | {board[4]} | {board[5]}
{board[6]} | {board[7]} | {board[8]}""")
        
while True:
    while board[player] != " ": #Does the player's turn
        player = int(input("What square do you want to play?: ")) - 1
        if board[player] != " ":
            print("That space is taken. Try again.")
            print_board()
        else:
            board[player] = "X"
            break
    
    if win_check("X") != " ": #Checks for win and tie, with priority to X
        print_board()
        print("Congratulations to our winner," + win_check("X") + "!")
        break
    if tie_check():
        print_board()
        print("Looks like that's a tie. Oh well!")
        break
    
    while board[bot] != " ": #Does the bot's turn
        bot = random.randint(0, 8)
    else:
        board[bot] = "O"
        print(f"The bot has chosen square {bot + 1}.")
    print_board()
    
    if win_check("O") != " ": #Checks for win and tie again, with priority to O
        print_board()
        print(f"Congratulations to our winner," + win_check("O") + "!")
        break
    if tie_check():
        print_board()
        print("Looks like that's a tie. Oh well!")
        break