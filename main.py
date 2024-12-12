import math
import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    """Checks if there's a winner or the game is a draw."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for draw
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return "Draw"
    return None

def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning."""
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif winner == "Draw":
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    """Finds the best move for the AI using the minimax algorithm."""
    best_val = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def update_button_text(buttons, board):
    """Updates the button text based on the board state."""
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def on_click(row, col, buttons, board, root):
    """Handles player moves and AI response."""
    if board[row][col] == " ":
        board[row][col] = "X"
        update_button_text(buttons, board)
        winner = check_winner(board)
        if winner:
            end_game(winner, root)
            return

        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
            update_button_text(buttons, board)
        winner = check_winner(board)
        if winner:
            end_game(winner, root)

def end_game(winner, root):
    """Ends the game and displays the winner."""
    if winner == "Draw":
        messagebox.showinfo("Game Over", "It's a draw!")
    else:
        messagebox.showinfo("Game Over", f"{winner} wins!")
    root.destroy()

def main():
    """Main function to create the GUI for the game."""
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                                      command=lambda row=i, col=j: on_click(row, col, buttons, board, root))
            buttons[i][j].grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    main()
