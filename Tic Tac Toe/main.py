import random
board = [
" ", " ", " ", 
" ", " ", " ", 
" ", " ", " "]

player = 0
bot = 0
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

print("""
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9""")

def tie_check():
    i = 0
    for play in board:
        if play == "X" or play == "O":
            i += 1
    if i != 9:
        i = 0
    return i == 9
def win_check():
    x_win = 0
    o_win = 0
    for win in wins:
        for play in wins:
            if board[play] == " ":
                x_win = 0
                o_win = 0
                break
            elif board[play] == "X":
                x_win += 1
            elif board[play] == "O":
                o_win += 1
        
        if x_win == 3:
            x_win = 0
            o_win = 0
            return "X"
        else:
            x_win = 0
            o_win = 0
        if o_win == 3:
            o_win = 0
            x_win = 0
            return "O"
        else:
            o_win = 0
            x_win = 0
    return " "
        
while True:
    while board[player] != " ":
        player = int(input("What square do you want to play?: ")) - 1
        if board[player] != " ":
            print("That space is taken. Try again.")
            print(f"""Current board: 
{board[0]} | {board[1]} | {board[2]}
{board[3]} | {board[4]} | {board[5]}
{board[6]} | {board[7]} | {board[8]}""")
        else:
            board[player] = "X"
            break
    
    if tie_check():
        print("Looks like that's a tie. Oh well!")
        break
    if win_check() != " ":
        print(f"Congratulations to our winner, {win_check()}!")
        break
    
    while board[bot] != " ":
        bot = random.randint(0, 8)
    else:
        board[bot] = "O"
        print(f"The bot has chosen square {bot + 1}.")
    print(f"""Current board: 
{board[0]} | {board[1]} | {board[2]}
{board[3]} | {board[4]} | {board[5]}
{board[6]} | {board[7]} | {board[8]}""")
    
    if tie_check():
        print("Looks like that's a tie. Oh well!")
        break
    if win_check() != " ":
        print(f"Congratulations to our winner, {win_check()}!")
        break