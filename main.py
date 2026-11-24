import tkinter as tk
from queens.board import Board
from queens.gui import QueensApp

regions = [
    [1,2,1,1,1,1,1,1],
    [1,2,1,3,1,1,1,1],
    [1,1,1,3,1,1,1,1],
    [1,4,4,4,1,1,1,1],
    [1,2,1,3,1,1,1,1],
    [1,1,1,3,1,1,1,1],
    [1,4,4,4,1,1,1,1],
    [1,1,1,4,5,1,1,1]
]

board = Board(regions)

root = tk.Tk()
QueensApp(root, board)
root.mainloop()