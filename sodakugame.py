import tkinter as tk
from tkinter import messagebox
import random
class Sudoku:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game")
        self.frame = tk.Frame(self.master, bg="#f0f0f0")
        self.frame.pack(padx=10, pady=10)
        self.grid = [[0]*9 for _ in range(9)]
        self.create_widgets()
        self.generate_sudoku()
    def create_widgets(self):
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.frame, width=5, font=('Arial', 24), justify='center', bd=2, relief='solid')
                entry.grid(row=i, column=j, padx=5, pady=5, ipady=10)
                self.entries[i][j] = entry
        self.check_button = tk.Button(self.frame, text="Check", command=self.check_solution, bg="#4CAF50", fg="white", font=('Arial', 14))
        self.check_button.grid(row=9, column=0, columnspan=3, pady=10)
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_game, bg="#f44336", fg="white", font=('Arial', 14))
        self.reset_button.grid(row=9, column=3, columnspan=3, pady=10)
        self.show_solution_button = tk.Button(self.frame, text="Show Solution", command=self.show_solution, bg="#2196F3", fg="white", font=('Arial', 14))
        self.show_solution_button.grid(row=9, column=6, columnspan=3, pady=10)
    def generate_sudoku(self):
        for _ in range(20):  # Number of initial clues
            x, y = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            if self.is_valid(x, y, num):
                self.grid[x][y] = num
                self.entries[x][y].insert(0, str(num))
    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == num:
                    return False
        return True
    def check_solution(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value and int(value) != self.grid[i][j]:
                    messagebox.showinfo("Result", "Incorrect solution!")
                    return
        messagebox.showinfo("Result", "Congratulations! Correct solution!")
    def show_solution(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:  # Only show the solution for filled values
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
                    self.entries[i][j].config(bg="#FFEB3B")  # Highlight the solution
    def reset_game(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.grid[i][j] = 0
        self.generate_sudoku()
if __name__ == "__main__":
    root = tk.Tk()
    app = Sudoku(root)
    root.mainloop()