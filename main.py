import math

board = [" " for _ in range(9)]

# Display Board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check Winner
def check_winner(b):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        a,b1,c = combo
        if b[a] == b[b1] == b[c] != " ":
            return b[a]

    if " " not in b:
        return "Tie"

    return None


# Minimax Algorithm
def minimax(board, depth, isMax):

    result = check_winner(board)

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Tie":
        return 0

    if isMax:

        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, False)
                board[i] = " "
                best = max(best, score)

        return best

    else:

        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True)
                board[i] = " "
                best = min(best, score)

        return best


# AI Best Move
def best_move():

    bestScore = -math.inf
    move = 0

    for i in range(9):

        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, 0, False)

            board[i] = " "

            if score > bestScore:
                bestScore = score
                move = i

    board[move] = "O"


# Main Game
while True:

    print_board()

    move = int(input("Enter position (1-9): ")) - 1

    if board[move] != " ":
        print("Invalid Move")
        continue

    board[move] = "X"

    winner = check_winner(board)

    if winner:
        print_board()
        print("Winner:", winner)
        break

    best_move()

    winner = check_winner(board)

    if winner:
        print_board()
        print("Winner:", winner)
        break