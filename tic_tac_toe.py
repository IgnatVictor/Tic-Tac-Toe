import sys


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for row in range(3):
        temp = []
        for column in range(3):

            temp.append(".")
        board.append(temp)

    return board


def get_input(text="Please enter row and column (ex: A2) "):

    rows = ["A", "B", "C"]
    cols = ["1", "2", "3"]

    inp = []
    user_text = input(text).upper()
    if user_text == "QUIT" or user_text == "Q":
        print("Thank you for playing! ")
        sys.exit()

    for char in user_text:
        if char != " ":
            inp.append(char)

    while inp[0] not in rows or inp[1] not in cols:
        inp = []
        user_text = input(text).upper()
        for char in user_text:
            if char != " ":
                inp.append(char)

    return (rows.index(inp[0]), cols.index(inp[1]))


def get_move(board, player):

    position = get_input()
    row = position[0]
    col = position[1]

    if board[row][col] == ".":
        return (row, col)
    else:
        position = get_input("Please try again, position already occupied ")
        # row = position[0]
        # col = position[1]

    return position


# def get_ai_move(board, player):
#     """Returns the coordinates of a valid move for player on board."""
#     row, col = 0, 0
#     return row, col


def mark(board, player, row, col):
    if board[row][col] == ".":
        board[row][col] = player

    return board


def has_won(board, player):
    combinations = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    temp = []

    for c in combinations:
        t = []
        for r in c:
            t.append(r == player)
        temp.append(all(t))

    return any(temp)


def is_full(board):
    ret = True
    for row in board:
        for col in row:
            if col == ".":
                ret = False

    return ret


def print_board(board):
    import os
    func = "clear" if os.uname().sysname == "Linux" else "cls"
    os.system(func)

    print(
        f"""
   1   2   3
A  {board[0][0]} | {board[0][1]} | {board[0][2]}
  ---+---+---
B  {board[1][0]} | {board[1][1]} | {board[1][2]}
  ---+---+---
C  {board[2][0]} | {board[2][1]} | {board[2][2]}
"""
    )


def print_result(board, winner):
    if has_won(board, winner):
        print(f"Congrats, {winner} wins!")
    else:
        print("It's a tie")
    sys.exit()


def tictactoe_game(mode="HUMAN-HUMAN"):
    board = init_board()
    player = "X"

    while True:
        print_board(board)
        row, col = get_move(board, player)
        board = mark(board, player, row, col)

        if has_won(board, player) or is_full(board):
            print_board(board)
            print_result(board, player)

        if player == "X":
            player = "0"
        else:
            player = "X"


# # def main_menu():
# #     tictactoe_game('HUMAN-HUMAN')


# if __name__ == '__main__':
#     main_menu()

# board = init_board()
# print(get_move(board, 0))
# print_board(board)
# test_board = [
#     ["0", "0", "0"],
#     ["0", "X", "0"],
#     ["X", "0", "X"],
# ]

# print(is_full(test_board))


tictactoe_game("HUMAN-HUMAN")
