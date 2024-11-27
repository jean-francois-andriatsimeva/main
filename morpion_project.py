def game_board():
    return [[" " for G in range(3)] for G in range(3)]

def print_game_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def add_symbol(board, row, col, symbol):
    if board[row][col] == " ":
        board[row][col] = symbol
        return True
    else:
        print("Case déjà remplie")
        return False

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] in ["X", "O"]:
            return f"Victoire: {row[0]}"

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ["X", "O"]:
            return f"Victoire: {board[0][col]}"

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ["X", "O"]:
        return f"Victoire: {board[0][0]}"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ["X", "O"]:
        return f"Victoire: {board[0][2]}"

    if all(cell != " " for row in board for cell in row):
        return "Match nul"

    return "Joueur suivant"

while True:
    board = game_board()
    print_game_board(board)

    while True:
        row = int(input("Entrer la ligne (0-2): "))
        col = int(input("Entrer la colonne (0-2): "))
        symbol = input("Choisi un symbole (X ou O): ").upper()

        if symbol not in ["X", "O"]:
            print("Symbole invalide, choisissez (X ou O).")
            continue

        if add_symbol(board, row, col, symbol):
            print_game_board(board)
            result = check_winner(board)
            print(result)

            if result != "Joueur suivant":
                break  

    replay = input("Voulez-vous jouer à nouveau ? (oui/non): ").lower()
    if replay != 'oui':
        break
