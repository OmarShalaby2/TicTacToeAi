import math
import tkinter as tk
from tkinter import messagebox
from minimax_aphabeta import minimax, check_winner


def best_move(board):
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
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def end_game(winner, root):
    if winner == "Draw":
        messagebox.showinfo("Game Over", "It's a draw!")
    else:
        messagebox.showinfo("Game Over", f"{winner} wins!")
    root.destroy()

def on_click(row, col, buttons, board, root):
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

def main():
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
